from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def test_heron_repo_keeps_control_description_and_message_contracts():
    assert (REPO_ROOT / "heron/heron_control/launch/control.launch").exists()
    assert (REPO_ROOT / "heron/heron_description/urdf/heron.urdf.xacro").exists()
    for msg in ("Drive.msg", "Sense.msg", "Status.msg"):
        assert (REPO_ROOT / "heron/heron_msgs/msg" / msg).exists()


def test_ig_handle_benchmark_config_aligns_imu_pose_with_dlio_geometry():
    config = (
        REPO_ROOT / "heron/heron_description/urdf/configs/ig_handle_benchmark"
    ).read_text(encoding="utf-8")

    assert 'HERON_IMU_XYZ="0.0656 0.0910 0.2030"' in config
    assert 'HERON_IMU_RPY="0 0 0"' in config


def test_description_launch_uses_portable_xacro_executable():
    launch = (REPO_ROOT / "heron/heron_description/launch/description.launch").read_text(
        encoding="utf-8"
    )

    assert "$(find xacro)/xacro" not in launch
    assert " xacro '$(find heron_description)/urdf/heron.urdf.xacro'" in launch
