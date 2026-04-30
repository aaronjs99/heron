from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def test_heron_repo_keeps_control_description_and_message_contracts():
    assert (REPO_ROOT / "heron/heron_control/launch/control.launch").exists()
    assert (REPO_ROOT / "heron/heron_description/urdf/heron.urdf.xacro").exists()
    for msg in ("Drive.msg", "Sense.msg", "Status.msg"):
        assert (REPO_ROOT / "heron/heron_msgs/msg" / msg).exists()
