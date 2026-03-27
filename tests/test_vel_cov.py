#!/usr/bin/env python3
import importlib
import os
import sys
import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock


class DummyTwistWithCovarianceStamped:
    def __init__(self):
        self.header = None
        self.twist = SimpleNamespace(twist=None, covariance=None)


_ORIG_MODULES = {
    name: sys.modules.get(name)
    for name in ("rospy", "geometry_msgs.msg", "sensor_msgs.msg")
}

mock_rospy = MagicMock()
mock_geometry_msgs = MagicMock()
mock_sensor_msgs = MagicMock()
mock_geometry_msgs.TwistWithCovarianceStamped = DummyTwistWithCovarianceStamped

sys.modules["rospy"] = mock_rospy
sys.modules["geometry_msgs.msg"] = mock_geometry_msgs
sys.modules["sensor_msgs.msg"] = mock_sensor_msgs

TEST_DIR = os.path.dirname(__file__)
SCRIPT_DIR = os.path.abspath(os.path.join(TEST_DIR, "..", "heron_control", "scripts"))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

import vel_cov  # noqa: E402

for _name, _module in _ORIG_MODULES.items():
    if _module is None:
        sys.modules.pop(_name, None)
    else:
        sys.modules[_name] = _module


class VelCovTests(unittest.TestCase):
    def setUp(self):
        sys.modules["rospy"] = mock_rospy
        sys.modules["geometry_msgs.msg"] = mock_geometry_msgs
        sys.modules["sensor_msgs.msg"] = mock_sensor_msgs
        importlib.reload(vel_cov)
        vel_cov.vel_pub = MagicMock()
        vel_cov.covariance = [0.0] * 36

    def tearDown(self):
        for _name, _module in _ORIG_MODULES.items():
            if _module is None:
                sys.modules.pop(_name, None)
            else:
                sys.modules[_name] = _module

    def test_navfix_cb_updates_position_covariance_diagonal(self):
        msg = SimpleNamespace(
            position_covariance=[1.1, 0.0, 0.0, 0.0, 2.2, 0.0, 0.0, 0.0, 3.3]
        )

        vel_cov.navfix_cb(msg)

        self.assertEqual(vel_cov.covariance[0], 1.1)
        self.assertEqual(vel_cov.covariance[7], 2.2)
        self.assertEqual(vel_cov.covariance[14], 3.3)

    def test_navsat_cb_publishes_twist_with_cached_covariance(self):
        vel_cov.covariance = [float(i) for i in range(36)]
        header = SimpleNamespace(frame_id="map")
        twist = SimpleNamespace(
            linear=SimpleNamespace(x=1.0), angular=SimpleNamespace(z=0.2)
        )
        msg = SimpleNamespace(header=header, twist=twist)

        vel_cov.navsat_cb(msg)

        published = vel_cov.vel_pub.publish.call_args[0][0]
        self.assertIs(published.header, header)
        self.assertIs(published.twist.twist, twist)
        self.assertEqual(published.twist.covariance, vel_cov.covariance)


if __name__ == "__main__":
    unittest.main()
