import pytest

from .challenge import make_inventory


@pytest.mark.parametrize(
    "shirts,expected",
    [
        (
            [
                "Purple Shirt",
            ],
            [
                "Purple Shirt Size: 1",
                "Purple Shirt Size: 2",
                "Purple Shirt Size: 3",
                "Purple Shirt Size: 4",
                "Purple Shirt Size: 5",
            ],
        ),
        (
            [
                "Purple Shirt",
                "Green Shirt",
            ],
            [
                "Purple Shirt Size: 1",
                "Purple Shirt Size: 2",
                "Purple Shirt Size: 3",
                "Purple Shirt Size: 4",
                "Purple Shirt Size: 5",
                "Green Shirt Size: 1",
                "Green Shirt Size: 2",
                "Green Shirt Size: 3",
                "Green Shirt Size: 4",
                "Green Shirt Size: 5",
            ],
        ),
    ],
)
def test_make_inventory(shirts, expected):
    assert make_inventory(shirts) == expected
