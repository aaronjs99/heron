Start the ROS 2 robot description with `ros2 launch heron_description description.launch.py`.
The `ig_handle_benchmark` profile uses the sensor-frame YAML explicitly selected
by `description.launch.py`; standalone launches retain the canonical IG Handle
file, and invalid profiles or frame files stop description generation before
xacro runs.

# File Structure

| File | Relevance | Dependencies | Used by |
| --- | --- | --- | --- |
| CMakeLists.txt | Installs HERON descriptions, meshes, launch files, and configuration profiles. | CMake 3.8+, ament_cmake | colcon build |
| package.xml | Declares HERON description package metadata and ROS dependencies. | ROS 2 | rosdep, CMakeLists.txt |
