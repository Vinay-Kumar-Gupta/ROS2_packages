import os
import launch
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, PythonExpression,Command
from launch.conditions import IfCondition

def generate_launch_description():
  nav2_launch_dir = os.path.join(get_package_share_directory('nav2_bringup'), 'launch')
  prefix_address = get_package_share_directory('test_bot_navigation') 
  params_file= os.path.join(prefix_address, 'config', 'nav2_params.yaml')
  map_file=LaunchConfiguration('map')
  slam=LaunchConfiguration('slam')  
  map_directory = os.path.join(get_package_share_directory(
        'test_bot_navigation'), 'maps','home_2.yaml')
  navigation_launch_cmd=IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_launch_dir, 'navigation_launch.py')),
            launch_arguments={'params_file': params_file,}.items())

  return LaunchDescription([
    launch.actions.DeclareLaunchArgument(name='slam', default_value='True',
                                            description='Flag to enable use_sim_time'),
    launch.actions.DeclareLaunchArgument(name='map',default_value=map_directory,
                                          description='Map to be used'),
    navigation_launch_cmd,  
     
    Node(
        package='nav2_map_server',
        condition=IfCondition(PythonExpression(['not ', slam])),
        executable='map_server',
        name='map_server',
        output='screen',
        parameters=[{'yaml_filename': map_file}]),
    Node(
        package='nav2_lifecycle_manager',
        condition=IfCondition(PythonExpression(['not ', slam])),
        executable='lifecycle_manager',
        name='lifecycle_manager_mapper',
        output='screen',
        parameters=[{'autostart': True},
                    {'node_names': ['map_server']}]),
  ]
)
