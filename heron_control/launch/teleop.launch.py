from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, EnvironmentVariable, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    namespace = LaunchConfiguration('namespace')
    joy_dev = LaunchConfiguration('joy_dev')
    joystick = LaunchConfiguration('joystick')
    use_interactive_marker = LaunchConfiguration('use_interactive_marker')

    teleop_yaml = PathJoinSubstitution(
        [FindPackageShare('heron_control'), 'config', 'teleop.yaml']
    )

    declare_args = [
        DeclareLaunchArgument('namespace', default_value=''),
        DeclareLaunchArgument(
            'joy_dev',
            default_value=EnvironmentVariable('HERON_JOY_DEVICE', default_value='/dev/input/js0')),
        DeclareLaunchArgument('joystick', default_value='false'),
        DeclareLaunchArgument('use_interactive_marker', default_value='false'),
    ]

    joystick_group = GroupAction(
        condition=IfCondition(joystick),
        actions=[
            Node(
                package='joy',
                executable='joy_node',
                name='joy_node',
                parameters=[teleop_yaml, {'dev': joy_dev}],
            ),
            Node(
                package='teleop_twist_joy',
                executable='teleop_node',
                name='teleop_twist_joy',
                parameters=[teleop_yaml],
                remappings=[('cmd_vel', [namespace, '/cmd_vel'])],
            ),
        ],
    )

    # Server for RViz Interactive Markers
    interactive_marker_node = Node(
        package='interactive_marker_twist_server',
        executable='marker_server',
        name='twist_marker_server',
        condition=IfCondition(use_interactive_marker),
        parameters=[{'link_name': [namespace, '/base_link']}],
        remappings=[('twist_marker_server/cmd_vel', 'cmd_vel_unscaled')],
    )

    return LaunchDescription(declare_args + [joystick_group, interactive_marker_node])