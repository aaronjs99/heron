# HERON Platform Packages

HERON is a ROS 1 platform repository for the Heron unmanned surface vehicle. It
contains vehicle description assets, ROS interfaces, and platform control
configuration.

## Quick start

With this repository's declared dependencies available in a Catkin workspace,
publish the vehicle description:

```bash
roslaunch heron_description description.launch
```

The launch file publishes the robot model for visualization and TF use.

## Documentation

- [Vehicle description](heron_description/README.md) covers the URDF/Xacro model and profiles.
- [Control](heron_control/README.md) covers platform control configuration.
- [Messages](heron_msgs/README.md) documents the ROS interfaces.

## Packages

| Package | Purpose |
| --- | --- |
| heron_description | URDF/Xacro, meshes, and vehicle configuration profiles |
| heron_msgs | Heron-specific ROS messages |
| heron_control | Platform control and state-estimation support |

## Repository scope

This repository contains the shared vehicle model, interfaces, and package
configuration. Keep local edits within these package boundaries and retain the
upstream file-level notices.

## License

Inherited platform code retains its BSD 3-Clause notices and file-level
attribution.

## File Structure

| File | Purpose | Dependencies | Used by |
| --- | --- | --- | --- |
| `.gitattributes` | Defines text and binary handling for this platform repository. | Git | Repository contributors |
| `.gitignore` | Excludes local build products and editor state. | Git | Repository contributors |
