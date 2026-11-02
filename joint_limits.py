"""Joint limit safety checks for the arm.

Angles are in degrees. Limits come from the mechanical spec."""

JOINT_LIMITS_DEG = {
    "base": (-180, 180),
    "shoulder": (-90, 95),
    "elbow": (-150, 150),
    "wrist": (-180, 180),
}


def within_limits(joint, angle_deg):
    """True if the angle is inside the joint's allowed range (inclusive)."""
    low, high = JOINT_LIMITS_DEG[joint]
    return low <= angle_deg <= high


def clamp(joint, angle_deg):
    """Pull an angle back inside the joint's allowed range."""
    low, high = JOINT_LIMITS_DEG[joint]
    return max(low, min(high, angle_deg))
