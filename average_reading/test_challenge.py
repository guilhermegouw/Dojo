import pytest
import math

from .challenge import average_temperature


@pytest.mark.parametrize(
    "temperatures,expected",
    [
        ([32, 68, 77, 104, 0, -40], 4.54),
    ],
)
def test_average_temperature(temperatures, expected):
    assert math.isclose(
        expected, average_temperature(temperatures), abs_tol=0.01
    )
