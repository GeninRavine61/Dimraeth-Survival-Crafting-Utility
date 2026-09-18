# Build: 2a615e2529004c4503925f5cb0e3bce7

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
