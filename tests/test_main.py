from src.main import add


def test_add_fun():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(5, 5) == 10

