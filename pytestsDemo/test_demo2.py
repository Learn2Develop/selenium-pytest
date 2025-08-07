import pytest


def test_firstprogram():
    print("Hello")

@pytest.mark.smoke
# @pytest.mark.skip
def test_secondprogram():
    a = 5
    b = 6
    assert a + 1 == b, "Addition does not match"


def test_creditcard2():
    print("Hello")