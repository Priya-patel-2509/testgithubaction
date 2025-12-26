from src.math_oprations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert add(0,2)==2

def test_sub():
    assert sub(3,4)==1
    assert sub(5,2)==3
    assert sub(1,0)==0
    assert sub(2,3)==-1

