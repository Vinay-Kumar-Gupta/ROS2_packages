from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription,DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
import os 
from ament_index_python import get_package_share_directory


def generate_launch_description():
    ld = LaunchDescription()

    v_bot_path = os.path.join(get_package_share_directory("v_bot_cleaner_description"),"launch/display.launch.py")
    slam_path = os.path.join(get_package_share_directory("test_bot_slam"),"launch/cartographer.launch.py")
    navigation_path = os.path.join(get_package_share_directory("test_bot_navigation"),"launch/navigation.launch.py")

   
    v_bot_cleaner_launch_file = IncludeLaunchDescription(PythonLaunchDescriptionSource(v_bot_path))


    slam_launch_file = IncludeLaunchDescription(PythonLaunchDescriptionSource(slam_path))


    navigation_launch_file = IncludeLaunchDescription(PythonLaunchDescriptionSource(navigation_path))

    ld.add_action(v_bot_cleaner_launch_file)
    ld.add_action(slam_launch_file)
    ld.add_action(navigation_launch_file)

    

    return ld
 
# from launch import LaunchDescription
# from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# from launch.substitutions import LaunchConfiguration
# import os 
# from ament_index_python import get_package_share_directory

# def generate_launch_description():
#     prefix_address = get_package_share_directory('test_bot_slam') 
#     config_directory = os.path.join(prefix_address, 'config')
#     ld = LaunchDescription()

#     # Get the paths of the launch files
#     v_bot_path = os.path.join(get_package_share_directory("v_bot_cleaner_description"),"launch/display.launch.py")
#     slam_path = os.path.join(get_package_share_directory("test_bot_slam"),"launch/cartographer.launch.py")
#     navigation_path = os.path.join(get_package_share_directory("test_bot_navigation"),"launch/navigation.launch.py")

#     # Include the launch files
#     v_bot_cleaner_launch_file = IncludeLaunchDescription(PythonLaunchDescriptionSource(v_bot_path))

#     # Pass arguments to the slam launch file
#     slam_launch_args = [
#         ("slam", LaunchConfiguration("slam_enabled"))
#     ]
#     slam_launch_file = IncludeLaunchDescription(PythonLaunchDescriptionSource(slam_path), launch_arguments=slam_launch_args)

#     # Pass arguments to the navigation launch file
#     navigation_launch_args = [
#         ("slam", LaunchConfiguration("slam_enabled")),
#         ("map", LaunchConfiguration("map_file"))
#     ]
#     navigation_launch_file = IncludeLaunchDescription(PythonLaunchDescriptionSource(navigation_path), launch_arguments=navigation_launch_args)

#     # Add actions to the LaunchDescription
#     ld.add_action(v_bot_cleaner_launch_file)
#     ld.add_action(slam_launch_file)
#     ld.add_action(navigation_launch_file)

#     # Declare launch arguments
#     ld.add_action(DeclareLaunchArgument("slam_enabled", default_value="True", description="Flag to enable SLAM"))
#     ld.add_action(DeclareLaunchArgument("map_file", default_value="", description="Map file to be used"))

#     # Add the declared arguments from slam launch file
#     ld.add_action(DeclareLaunchArgument("resolution", default_value="0.05", description="Configure the resolution"))
#     ld.add_action(DeclareLaunchArgument("publish_period_sec", default_value="1.0", description="Publish period in seconds"))

#     # Add the declared arguments from navigation launch file
#     ld.add_action(DeclareLaunchArgument("params_file", default_value="", description="Path to the nav2 parameters file"))

#     return ld
