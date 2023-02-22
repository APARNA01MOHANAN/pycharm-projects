#phase 1

import essentials as ab
import pytest
def test_monkey_trouble():
    assert ab.monkey_trouble(True,True)== True
    assert ab.monkey_trouble(False, True) == False
    assert ab.monkey_trouble(True, False) == False
    assert ab.monkey_trouble(False, False) == True

@pytest.mark.parametrize("a_smile,b_smile",[(True,True),(False,True),(False,True),(False,False)])
def test_monkey_trouble(a_smile,b_smile):
    assert oe.monkey_trouble(True, True) == True
    assert oe.monkey_trouble(False, True) == False
    assert oe.monkey_trouble(True, False) == False
    assert oe.monkey_trouble(False, False) == True

#phase 2
import essentials as txt
@pytest.mark.skip(reason="still to enhance")
def test_string_bits():
    assert txt.string_bits("hello") == 'hlo'
    assert txt.string_bits("hi") == 'h'
    assert txt.string_bits("heeololeo") == 'hello'
#phase 3

import essentials as oe
import pytest
@pytest.fixture
def values():
    a=[1, 2, 3],[1,2,3],[5,6,7]
    b=[3, 4, 5],[4,3,2],[9,8,7]
    return a
    return b
def test_common_end(values):
    assert oe.common_end(a=[1, 2, 3], b=[3, 4, 5])=="False"
    assert oe.common_end(a=[1, 2, 3], b=[4, 2, 3])=="True"
    assert oe.common_end(a=[5, 6, 7], b=[9, 8, 7])=="True"
