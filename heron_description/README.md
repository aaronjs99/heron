# File Structure

| File | Relevance | Dependencies | Used by |
| --- | --- | --- | --- |
| CMakeLists.txt | Defines installation of HERON descriptions, meshes, launch files, and configuration profiles. | CMake 3.0.2+, catkin | catkin build |
| package.xml | Declares HERON description package metadata and ROS dependencies. | ROS | rosdep, CMakeLists.txt |
