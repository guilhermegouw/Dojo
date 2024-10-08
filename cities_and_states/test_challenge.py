import pytest
from challenge import count_special_pairs


@pytest.mark.parametrize(
    ("cities", "expected"),
    [
        (["SCRANTON PA", "PARKER SC"], 1),
        (["HOUSTON TX", "AUSTIN TX", "NEWYORK NY"], 0),
        (
            ["SCRANTON PA", "PARKER SC", "HARRISBURG PA", "SALEM SC"],
            1,
        ),
        (["SCRANTON PA", "HARRISBURG PA"], 0),
        (
            [
                "SCRANTON PA",
                "PARKER SC",
                "HARRISBURG PA",
                "COLUMBIA SC",
                "NEWARK NJ",
                "ATLANTA GA",
                "ALBANY NY",
            ],
            1,
        ),
        (["SCRANTON PA", "PARKER TX", "NEWARK NJ", "ALBANY GA"], 0),
    ],
)
def test_count_special_pairs(cities, expected):
    assert count_special_pairs(cities) == expected
