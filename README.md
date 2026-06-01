# HERON

This package family provides the platform description and core ROS interfaces
for the Clearpath Heron USV.

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

## Benchmark Profile

This workspace carries an explicit benchmark profile for the IG Handle Heron in:

- `heron_description/urdf/configs/ig_handle_benchmark`

That file is where draft, inertia, added-mass, and damping changes are kept for
the full simulation stack. It is the preferred place to tune the vehicle
benchmark instead of burying those changes in launch-time ad hoc parameters.

## Tests

This repo now also carries package-level tests under `tests/`, including the
velocity covariance helper checks used by the broader workspace.

## Typical Use

```bash
roslaunch heron_description description.launch
```

That brings up the robot description so the rest of the stack can publish state,
spawn the vehicle, or visualize the model.

## Role In The Workspace

HERON is the common platform layer underneath:

- ORACLE
- MARINER
- simulator integration
- control and sensing packages

It gives the rest of the workspace a consistent vehicle definition.
