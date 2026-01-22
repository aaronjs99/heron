# HERON: Unmanned Surface Vessel Platform Framework

## Abstract

This repository serves as the foundational meta-package for the Clearpath Heron USV within the SLAM GRANDE ecosystem. It encapsulates the high-fidelity digital representation of the platform, including kinematic and dynamic properties (URDF/SDF), specialized message definitions, and low-level control configurations essential for operational deployment.

## Constituent Modules

*   **heron_description**: Comprehensive physical models, mesh geometries, and collision topologies.
*   **heron_msgs**: Formal definitions for RPC and asynchronous communication, including thruster command protocols and system status reports.
*   **heron_control**: Implementation of Extended Kalman Filter (EKF) localization and primary control manifold configurations.

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
