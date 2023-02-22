'''import pytest
def summation(a,b):
    result=a+b
    return result
@pytest.mark.skip(reason="more to enhance")
def test_summation():
    num1=10
    num2=5
    actualsum=summation(num1,num2)
    expectedsum=15
    assert actualsum==expectedsum
@pytest.mark.skip(reason="more to enhance")
def test_summation():
    num1=10
    num2=5
    assert actualsum(num1,num2)==15

def mul(a,b):
    res=a*b
    return res
def div(a,b):
    res=a/b
    return res
def test_calculate():
    n1=10
    n2=5
    actualout=mul(n1,n2)
    expectedout=8
    assert actualout==expectedout
def test_calculate():
    n1=4
    n2=2
    assert mul(n1,n2)==8
    assert div(n1,n2)!=2'''


'''def name(string):
    string=" "
    if "python" in string:
        print("true")
    else:
        print("false")
def test_name():
    s="python has pytest"
    actual==name(s)
    expect=="true"
    assert actual==expect'''
'''def function(a,b):
    if(a>b):
        print("a is greater than b")
    elif(a==b):
        print("a is equal to b")
    elif(a<b):
        print("a is smaller to b")
    else:
        print("a is not equal to b")
def test_fun():
    n1=2
    n2=6
    actualout=function(n1,n2)
    expectedout='a is smaller to b'
    assert actualout==expectedout'''
import pytest
import math as m
@pytest.mark.parametrize("num,nroot",[(16,4),(9,3),(4,2),(1,1)])
def testmysqrtpara(num,nroot):
    assert m.sqrt(num)==nroot