# File Structure

| File | Relevance | Dependencies | Used by |
| --- | --- | --- | --- |
| CMakeLists.txt | Installs the HERON control launch/configuration surfaces and the `vel_cov.py` runtime node. | CMake 3.0.2+, catkin | catkin build |
| package.xml | Declares HERON control package metadata and ROS dependencies. | ROS | rosdep, CMakeLists.txt |
