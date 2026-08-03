# File Structure

| File | Relevance | Dependencies | Used by |
| --- | --- | --- | --- |
| CMakeLists.txt | Defines the HERON control package build and installation surface. | catkin, robot_localization, rospy | catkin build |
| package.xml | Declares HERON control package metadata and ROS dependencies. | ROS | rosdep, CMakeLists.txt |
