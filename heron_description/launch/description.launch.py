from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import (
    LaunchConfiguration,
    PythonExpression,
    Command,
    PathJoinSubstitution,
)
from launch_ros.actions import Node, PushRosNamespace
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    hydro_debug = LaunchConfiguration('hydro_debug')
    config = LaunchConfiguration('config')
    sensor_frames_file = LaunchConfiguration('sensor_frames_file')
    simulation = LaunchConfiguration('simulation')
    namespace = LaunchConfiguration('namespace')
    run_robot_state_publisher = LaunchConfiguration('run_robot_state_publisher')

    declare_args = [
        DeclareLaunchArgument('hydro_debug', default_value='0'),
        DeclareLaunchArgument('config', default_value='base'),
        DeclareLaunchArgument(
            'sensor_frames_file', default_value='',
            description='Optional canonical sensor-frame YAML consumed by '
                        'geometry-exporting vehicle profiles.'),
        DeclareLaunchArgument('simulation', default_value='false'),
        DeclareLaunchArgument('namespace', default_value=''),
        DeclareLaunchArgument('run_robot_state_publisher', default_value='true'),
    ]

    env_run_script = PathJoinSubstitution(
        [FindPackageShare('heron_description'), 'env_run.sh']
    )
    config_dir = PathJoinSubstitution(
        [FindPackageShare('heron_description'), 'urdf', 'configs', config]
    )
    xacro_file = PathJoinSubstitution(
        [FindPackageShare('heron_description'), 'urdf', 'heron.urdf.xacro']
    )

    robot_description_no_ns = Command([
        "env HERON_SENSOR_FRAMES_FILE='", sensor_frames_file, "' ",
        env_run_script, ' ', config_dir, ' ',
        "xacro '", xacro_file, "' ",
        'debug:=', hydro_debug, ' ',
        'simulation:=', simulation,
    ])

    robot_description_with_ns = Command([
        "env HERON_SENSOR_FRAMES_FILE='", sensor_frames_file, "' ",
        env_run_script, ' ', config_dir, ' ',
        "xacro '", xacro_file, "' ",
        'debug:=', hydro_debug, ' ',
        'simulation:=', simulation, ' ',
        'namespace:=', namespace, ' ',
        'suffix_ns:=', namespace, '/',
    ])

    # A joint state publisher plugin already is started with the model, no need to use the default joint state publisher
    # Publish robot model for ROS
    no_namespace_group = GroupAction(
        condition=IfCondition(PythonExpression(["'", namespace, "' == ''"])),
        actions=[
            PushRosNamespace(namespace),
            Node(
                package='robot_state_publisher',
                executable='robot_state_publisher',
                name='robot_state_publisher',
                respawn=False,
                output='screen',
                condition=IfCondition(run_robot_state_publisher),
                parameters=[{'robot_description': ParameterValue(robot_description_no_ns, value_type=str)}],
            ),
        ],
    )

    with_namespace_group = GroupAction(
        condition=UnlessCondition(PythonExpression(["'", namespace, "' == ''"])),
        actions=[
            PushRosNamespace(namespace),
            Node(
                package='robot_state_publisher',
                executable='robot_state_publisher',
                name='robot_state_publisher',
                respawn=False,
                output='screen',
                condition=IfCondition(run_robot_state_publisher),
                parameters=[{'robot_description': ParameterValue(robot_description_with_ns, value_type=str)}],
            ),
        ],
    )

    return LaunchDescription(declare_args + [no_namespace_group, with_namespace_group])