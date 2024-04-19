from git.source.calculator import square
import pytest


def testSq():
    assert square(2) == 4
    assert square(3) == 9


def testNeg():
    assert square(-2) == 4
    assert square(-3) == 9


def testZero():
    assert square(0) == 0


def testStr():
    with pytest.raises(TypeError):
        square("cat")
# enter pytest tCalc in the terminal to test assertions
