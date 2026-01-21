# HERON: Unmanned Surface Vessel Platform

[![ROS](https://img.shields.io/badge/ROS-Noetic-blue)](http://wiki.ros.org/noetic)
[![License](https://img.shields.io/badge/license-BSD-lightgrey)]()

## Abstract

This is the meta-package for the Clearpath Heron USV found in the SLAM GRANDE system. It contains the physical descriptions (URDF), message definitions, and low-level control configurations required to operate the robot.

## Sub-Packages

*   **heron_description**: URDF models, meshes, and collision geometries.
*   **heron_msgs**: Custom ROS messages for thruster commands and status reports.
*   **heron_control**: EKF localization and control configuration.

## Related Packages

*   **heron_simulator**: Gazebo simulation environment.
*   **heron_controller**: C++ implementation of the force allocation and dynamic control.

## Usage

To launch the base description:
```bash
roslaunch heron_description description.launch
```

## Citation

```bibtex
@misc{heron_ros,
  author = {Clearpath Robotics},
  title = {Heron USV ROS Integration},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/heron/heron}}
}
```
