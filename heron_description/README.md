The `ig_handle_benchmark` profile uses the sensor-frame YAML explicitly selected
by `description.launch`; standalone launches retain the canonical IG Handle file,
and invalid profiles or frame files stop description generation before xacro runs.

# File Structure

| File | Relevance | Dependencies | Used by |
| --- | --- | --- | --- |
| CMakeLists.txt | Defines installation of HERON descriptions, meshes, launch files, and configuration profiles. | CMake 3.0.2+, catkin | catkin build |
| package.xml | Declares HERON description package metadata and ROS dependencies. | ROS | rosdep, CMakeLists.txt |
