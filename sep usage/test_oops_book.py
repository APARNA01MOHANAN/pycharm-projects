
import oops_book as ob
import pytest

@pytest.mark.skip(reason="still to enhance")
def test_in_stock():
    assert ob.in_stock()=='True'

