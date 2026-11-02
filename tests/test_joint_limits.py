import random

import pytest

from joint_limits import JOINT_LIMITS_DEG, clamp, within_limits


def test_base_inside_limits():
    assert within_limits("base", 0)


def test_base_outside_limits():
    assert not within_limits("base", 200)


def test_clamp_pulls_angle_back_inside():
    assert clamp("elbow", 170) == 150


def test_unknown_joint_raises():
    with pytest.raises(KeyError):
        within_limits("finger", 0)


@pytest.mark.endurance
def test_endurance_random_angles_always_clamped_inside():
    rng = random.Random(42)
    for _ in range(200_000):
        joint = rng.choice(list(JOINT_LIMITS_DEG))
        angle = rng.uniform(-400, 400)
        assert within_limits(joint, clamp(joint, angle))
