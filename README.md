# HERON Platform Packages

This repository contains inherited Heron platform description and core ROS
interfaces used by the GRANDE workspace. GRANDE consumes these interfaces but
does not use this repository as the authority for real sensor extrinsics,
runtime networking, or MCU firmware behavior.

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

## File Structure

| File | Relevance | Dependencies | Used by |
| --- | --- | --- | --- |
| .gitattributes | Forces Linux line endings for executable xacro environment profiles. | Git | HERON Simulator xacro launch |
