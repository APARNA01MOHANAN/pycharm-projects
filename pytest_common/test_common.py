import common as oe
def test_common_end():
    assert oe.common_end(a=[1, 2, 3], b=[3, 4, 5])=="False"
    assert oe.common_end(a=[1, 2, 3], b=[4, 2, 3])=="True"
    assert oe.common_end(a=[5, 6, 7], b=[9, 8, 7])=="True"