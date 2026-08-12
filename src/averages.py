"""Small dependency-free statistics helpers used by the workflow sandbox."""

from collections.abc import Sequence
from math import fsum


def mean(values: Sequence[float]) -> float:
    """Return the arithmetic mean of a non-empty sequence."""
    if len(values) == 0:
        raise ValueError("mean requires at least one value")
    return fsum(values) / len(values)
