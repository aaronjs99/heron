import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction, OpaqueFunction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, EnvironmentVariable, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    enable_ekf = LaunchConfiguration('enable_ekf')
    enable_navsat = LaunchConfiguration('enable_navsat')
    startup_delay_sec = LaunchConfiguration('startup_delay_sec')
    config_extras = LaunchConfiguration('config_extras')

    default_config_extras = PathJoinSubstitution(
        [FindPackageShare('heron_control'), 'config', 'empty.yaml']
    )

    # TODO(ROS2 migration): config_extras is declared below but not applied to any node
    declare_args = [
        DeclareLaunchArgument(
            'config_extras',
            default_value=EnvironmentVariable('HERON_CONFIG_EXTRAS', default_value=default_config_extras)),
        DeclareLaunchArgument('enable_ekf', default_value='false'),
        DeclareLaunchArgument('enable_navsat', default_value='false'),
        DeclareLaunchArgument('startup_delay_sec', default_value='0.0'),
    ]

    # A plain substitution list (no OpaqueFunction needed) — pure string
    # concatenation, resolved the same way PathJoinSubstitution/Command are.
    startup_prefix = ['bash -lc \'sleep ', startup_delay_sec, '; exec "$0" "$@"\'']

    ekf_group = GroupAction(
        condition=IfCondition(enable_ekf),
        actions=[
            Node(
                package='robot_localization',
                executable='ekf_node',
                name='ekf_localization_node',
                prefix=startup_prefix,
                parameters=[PathJoinSubstitution(
                    [FindPackageShare('heron_control'), 'config', 'robot_localization.yaml'])],
            ),
        ],
    )

    def make_datum_params(context):
        gps_datum = os.environ.get('GPS_DATUM', '43.4720948, -80.5592608')
        lat_str, lon_str = [p.strip() for p in gps_datum.split(',')]
        datum = [float(lat_str), float(lon_str), 0.0]
        wait_for_datum = os.environ.get('GPS_DATUM', '') != ''
        return [
            Node(
                package='robot_localization',
                executable='navsat_transform_node',
                name='navsat_transform_node',
                respawn=False,
                output='screen',
                prefix=startup_prefix,
                parameters=[
                    PathJoinSubstitution(
                        [FindPackageShare('heron_control'), 'config', 'navsat_config.yaml']),
                    {'datum': datum, 'wait_for_datum': wait_for_datum},
                ],
                remappings=[('gps/fix', 'navsat/fix')],
            ),
        ]

    navsat_group = GroupAction(
        condition=IfCondition(enable_navsat),
        actions=[OpaqueFunction(function=make_datum_params)],
    )

    vel_cov_node = Node(
        package='heron_control',
        executable='vel_cov.py',
        name='navsat_vel_cov',
        condition=IfCondition(enable_navsat),
        prefix=startup_prefix,
    )

    return LaunchDescription(
        declare_args + [ekf_group, navsat_group, vel_cov_node]
    )