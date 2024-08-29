from challenge import get_cone_volume


def test_get_cone_volume():
    assert get_cone_volume(1, 1) == 1.0471975511965976
    assert get_cone_volume(2, 2) == 8.377580409572781
    assert get_cone_volume(3, 3) == 28.274333882308138
    assert get_cone_volume(4, 4) == 67.02064327658225
    assert get_cone_volume(5, 5) == 130.89969389957471
    assert get_cone_volume(6, 6) == 226.1946710584651
