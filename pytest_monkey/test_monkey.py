import monkey as oe
import pytest

def test_monkey_trouble():
    assert oe.monkey_trouble(True,True)== True
    assert oe.monkey_trouble(False, True) == False
    assert oe.monkey_trouble(True, False) == False
    assert oe.monkey_trouble(False, False) == True
@pytest.mark.parametrize("a_smile,b_smile",[(True,True),(False,True),(False,True),(False,False)])
def test_monkey_trouble(a_smile,b_smile):
    assert oe.monkey_trouble(True, True) == True
    assert oe.monkey_trouble(False, True) == False
    assert oe.monkey_trouble(True, False) == False
    assert oe.monkey_trouble(False, False) == True