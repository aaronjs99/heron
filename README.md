# HERON

This package family provides the platform description and core ROS interfaces
for the Clearpath Heron USV used throughout SLAM GRANDE.

## What Lives Here

- `heron_description`
  - URDF/Xacro, meshes, and physical layout
- `heron_msgs`
  - platform-specific ROS messages
- `heron_control`
  - state-estimation and control-related support

## What This Package Is For

If you need the vehicle’s:

- geometry
- platform messages
- base platform conventions

this is the right place to start.

If you need the simulation environment, use `heron_simulator`.
If you need the low-level controller implementation, use `heron_controller`.

## Typical Use

```bash
roslaunch heron_description description.launch
```

That brings up the robot description so the rest of the stack can publish state,
spawn the vehicle, or visualize the model.

## Role In SLAM GRANDE

HERON is the common platform layer underneath:

- ORACLE
- MARINER
- simulator integration
- control and sensing packages

It gives the rest of the workspace a consistent vehicle definition.
