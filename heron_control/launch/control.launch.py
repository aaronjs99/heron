import math
import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction, TimerAction
from launch.conditions import IfCondition
from launch.substitutions import (
    EnvironmentVariable,
    LaunchConfiguration,
    PathJoinSubstitution,
)
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare


def _launch_nodes(context):
    delay = float(
        context.perform_substitution(LaunchConfiguration("startup_delay_sec"))
    )
    if not math.isfinite(delay) or delay < 0.0:
        raise RuntimeError("startup_delay_sec must be a finite non-negative number")

    config_extras = LaunchConfiguration("config_extras")
    imu_topic = LaunchConfiguration("imu_topic")
    enable_ekf = LaunchConfiguration("enable_ekf")
    enable_navsat = LaunchConfiguration("enable_navsat")
    use_sim_time = ParameterValue(LaunchConfiguration("use_sim_time"), value_type=bool)

    ekf = Node(
        package="robot_localization",
        executable="ekf_node",
        name="ekf_localization_node",
        output="screen",
        condition=IfCondition(enable_ekf),
        parameters=[
            PathJoinSubstitution(
                [FindPackageShare("heron_control"), "config", "robot_localization.yaml"]
            ),
            config_extras,
            {"imu0": imu_topic},
            {"use_sim_time": use_sim_time},
        ],
    )

    navsat_enabled = IfCondition(enable_navsat).evaluate(context)
    datum = [0.0, 0.0, 0.0]
    wait_for_datum = False
    if navsat_enabled:
        gps_datum = os.environ.get("GPS_DATUM", "43.4720948, -80.5592608")
        try:
            latitude, longitude = (float(part.strip()) for part in gps_datum.split(","))
        except (TypeError, ValueError) as exc:
            raise RuntimeError("GPS_DATUM must contain latitude, longitude") from exc
        if not -90.0 <= latitude <= 90.0 or not -180.0 <= longitude <= 180.0:
            raise RuntimeError("GPS_DATUM latitude/longitude is outside valid bounds")
        datum = [latitude, longitude, 0.0]
        wait_for_datum = bool(os.environ.get("GPS_DATUM", ""))

    navsat = Node(
        package="robot_localization",
        executable="navsat_transform_node",
        name="navsat_transform_node",
        output="screen",
        condition=IfCondition(enable_navsat),
        parameters=[
            PathJoinSubstitution(
                [FindPackageShare("heron_control"), "config", "navsat_config.yaml"]
            ),
            config_extras,
            {
                "datum": datum,
                "wait_for_datum": wait_for_datum,
                "use_sim_time": use_sim_time,
            },
        ],
        remappings=[("gps/fix", "navsat/fix"), ("imu/data", imu_topic)],
    )

    velocity_covariance = Node(
        package="heron_control",
        executable="vel_cov.py",
        name="navsat_vel_cov",
        output="screen",
        condition=IfCondition(enable_navsat),
        parameters=[
            {"navsat_velocity_topic": LaunchConfiguration("navsat_velocity_topic")}
        ],
    )
    nodes = [ekf, navsat, velocity_covariance]
    return [TimerAction(period=delay, actions=nodes)] if delay > 0.0 else nodes


def generate_launch_description():
    default_extras = PathJoinSubstitution(
        [FindPackageShare("heron_control"), "config", "empty.yaml"]
    )
    return LaunchDescription(
        [
            DeclareLaunchArgument("enable_ekf", default_value="false"),
            DeclareLaunchArgument("enable_navsat", default_value="false"),
            DeclareLaunchArgument("use_sim_time", default_value="false"),
            DeclareLaunchArgument(
                "navsat_velocity_topic", default_value="navsat/velocity"
            ),
            DeclareLaunchArgument("startup_delay_sec", default_value="0.0"),
            DeclareLaunchArgument(
                "imu_topic",
                default_value="/sensors/imu/data",
                description=(
                    "IMU input; the selected description must publish the measured "
                    "base_link-to-imu_link transform"
                ),
            ),
            DeclareLaunchArgument(
                "config_extras",
                default_value=EnvironmentVariable(
                    "HERON_CONFIG_EXTRAS", default_value=default_extras
                ),
                description=(
                    "ROS 2 parameter YAML with node selectors for "
                    "ekf_localization_node and/or navsat_transform_node"
                ),
            ),
            OpaqueFunction(function=_launch_nodes),
        ]
    )
