import pytest
from challenge import count_unique_emails


@pytest.mark.parametrize(
    ("emails", "expected"),
    [
        (["daniel.zingaro@gmail.com"], 1),
        (["daniel.zingaro@gmail.com", "daniel.zingaro+book@gmail.com"], 1),
        (
            [
                "daniel.zingaro@gmail.com",
                "daniel.zingaro+book@gmail.com",
                "daniel.zin.garo.@gmail.com",
            ],
            1,
        ),
    ],
)
def test_get_num_of_unique_emails(emails, expected):
    assert count_unique_emails(emails) == expected
