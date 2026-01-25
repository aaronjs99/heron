# heron_msgs

**Common ROS message definitions for the Heron USV platform.**

[![ROS](https://img.shields.io/badge/ROS-Noetic-blue)](http://wiki.ros.org/noetic)

## Overview

This package provides standardized message types for communication between the Heron USV's microcontroller unit (MCU), control software, and higher-level autonomy stacks.

## Messages

### heron_msgs/Course

**Absolute heading and velocity command.**

```
float32 yaw     # Yaw in radians counter-clockwise from true east
float32 speed   # Velocity in m/s (negative = reverse)
```

---

### heron_msgs/Drive

**Raw thruster command transmitted to the MCU.**

Published on `/cmd_drive`.

```
float32 left    # Left thruster effort [-1.0, 1.0]
float32 right   # Right thruster effort [-1.0, 1.0]
```

---

### heron_msgs/Helm

**Thrust percentage and yaw rate command.**

```
float32 thrust    # Thrust amount [-1.0, 1.0]
float32 yaw_rate  # Yaw rate in rad/s (positive = port turn)
```

---

### heron_msgs/Sense

**MCU sensor feedback transmitted on `/sense`.**

```
Header header
float32 battery        # Battery voltage (V)
float32 current_left   # Left motor current (A)
float32 current_right  # Right motor current (A)
uint8 rc               # RC override status bitfield (RC_INRANGE=1, RC_INUSE=2)
uint16 rc_throttle     # RC throttle pulse width
uint16 rc_rotation     # RC rotation pulse width
uint16 rc_enable       # RC enable pulse width
```

---

### heron_msgs/Status

**System status transmitted at 1Hz on `/status`.**

```
Header header
string hardware_id           # Firmware commit hash
duration mcu_uptime          # Time since MCU power-on
duration connection_uptime   # Time since rosserial connection
float32 pcb_temperature      # PCB temperature (°C)
float32 user_current         # User current draw (A, averaged)
float32 user_power_consumed  # User power since startup (Wh)
float32 motor_power_consumed # Motor power since startup (Wh)
float32 total_power_consumed # Total power since startup (Wh)
```

## Usage

```python
from heron_msgs.msg import Drive

msg = Drive()
msg.left = 0.5
msg.right = 0.5
drive_pub.publish(msg)
```
