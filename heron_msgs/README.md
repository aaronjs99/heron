# heron_msgs

`heron_msgs` defines the Heron-specific message interfaces used by the platform,
controller, simulator, and navigation bridge.

## Common Messages

| Message | Purpose |
| --- | --- |
| `heron_msgs/Drive` | Left/right thruster command |
| `heron_msgs/Helm` | Higher-level thrust and yaw-rate command |
| `heron_msgs/Course` | Heading and forward-speed command |
| `heron_msgs/Sense` | MCU feedback, battery state, currents, and RC override state |
| `heron_msgs/Status` | Platform health and power-consumption summary |

## Example

```python
from heron_msgs.msg import Drive

msg = Drive()
msg.left = 0.5
msg.right = 0.5
drive_pub.publish(msg)
```

This package intentionally contains messages only. Control policy belongs in
the controller and navigation packages.

The message definitions describe transport fields, not calibrated physical
thrust. Treat `Drive.left` and `Drive.right` as normalized command interfaces;
their relation to current, thrust, and vehicle motion must be established from
validated platform evidence outside this message package.

## File Structure

| File | Relevance | Dependencies | Used by |
| --- | --- | --- | --- |
| CMakeLists.txt | Declares HERON message generation and catkin exports. | catkin, message_generation, std_msgs | catkin build |
| package.xml | Declares HERON message package metadata and ROS dependencies. | ROS Noetic | CMakeLists.txt, rosdep |
