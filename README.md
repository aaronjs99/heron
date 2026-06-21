# HERON Platform Packages

This repository contains the Heron platform description and core ROS interfaces
used by the GRANDE workspace.

## Packages

| Package | Purpose |
| --- | --- |
| `heron_description` | URDF/Xacro, meshes, and vehicle configuration profiles |
| `heron_msgs` | Heron-specific ROS messages |
| `heron_control` | Platform control and state-estimation support |

## Benchmark Profile

The IG Handle benchmark vehicle profile lives at:

```text
heron_description/urdf/configs/ig_handle_benchmark
```

Use that profile for simulation and full-stack integration work that needs the
current hull, inertia, added-mass, damping, and sensor-mount assumptions.

## Typical Use

```bash
roslaunch heron_description description.launch
```

The description launch publishes the robot model for visualization, simulation,
and TF integration.

## Workspace Role

HERON provides the shared platform layer under:

- MARINER navigation and drive bridging
- HERON Simulator vehicle spawn
- IG Handle sensor-frame integration
- ORACLE mission execution context

Keep platform geometry here; keep simulation worlds in `heron_simulator` and
runtime sensing in `ig_handle`.
