# File Structure

| File | Relevance | Dependencies | Used by |
| --- | --- | --- | --- |
| CMakeLists.txt | Installs the HERON control launch/configuration surfaces and the `vel_cov.py` runtime node. | CMake 3.8+, ament_cmake | colcon build |
| package.xml | Declares HERON control package metadata and ROS dependencies, including its `rclpy` runtime. | ROS 2 | rosdep, CMakeLists.txt |

## Estimator ownership

The stock HERON EKF/navsat stack and GRANDE's DLiO/MARINER stack are separate
operating modes. `control.launch.py` keeps the stock estimator disabled by
default.  When explicitly enabled, both stock nodes consume the canonical
external IMU topic, `/sensors/imu/data`.

A matching topic is only half of the IMU contract.  The robot description used
for that run must publish the measured `base_link -> imu_link` transform.  Do
not enable or restart the stock estimator against the stock identity transform
on the IG Handle boat.  GRANDE real DLiO bringup performs its own deliberate
model/TF handoff, stops the stock EKF/navsat authorities, and publishes
`/state/odometry_3dof` as the operator-facing odometry source.

The NavSat velocity adapter consumes the relative `navsat/velocity` topic by
default, matching the Heron description. Override `navsat_velocity_topic` when
a sensor driver publishes a different topic. When launching under a namespace,
provide a matching `imu_topic` and `config_extras` with the namespaced frames.

The stock stack may be restored only through a deliberate stock recovery or
boat reboot using a geometry-correct robot description.  Never run both
estimator/TF authority sets together.
