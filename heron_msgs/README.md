# heron_msgs

ROS message definitions for the Heron platform.

These messages sit between the vehicle-specific layers and the rest of the
stack, especially for drive commands and platform health.

## Common Messages

### `heron_msgs/Drive`

Low-level left/right thruster command.

| Field | Meaning |
|---|---|
| `left` | Left thruster effort |
| `right` | Right thruster effort |

### `heron_msgs/Helm`

Higher-level thrust plus yaw-rate command.

### `heron_msgs/Course`

Heading plus forward-speed command.

### `heron_msgs/Sense`

MCU feedback including battery, currents, and RC override state.

### `heron_msgs/Status`

Platform health and power-consumption summary.

## Example

```python
from heron_msgs.msg import Drive

msg = Drive()
msg.left = 0.5
msg.right = 0.5
drive_pub.publish(msg)
```

This package is intentionally small: it exists so the rest of the workspace can
share a consistent Heron-specific message contract.
