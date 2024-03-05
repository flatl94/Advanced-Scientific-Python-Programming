import pytest
import simple_math

print('This script aims to test the methods in  "simple_math.py".')
a = -1
b = 4


@pytest.mark.parametrize("a,b", [(-1,4), (2,5), (0,6)])
def test_simple_add(a,b):
    assert simple_math.simple_add(a,b) == a+b

@pytest.mark.parametrize("a,b", [(-1,4), (2,5), (0,6)])  
def test_simple_sub(a,b):
    assert simple_math.simple_sub(a,b) == a-b

@pytest.mark.parametrize("a,b", [(-1,4), (2,5), (0,6)])
def test_simple_mult(a,b):
    assert simple_math.simple_mult(a,b) == a*b
    
@pytest.mark.parametrize("a,b", [(-1,4), (2,5), (0,6)])
def test_simple_div(a,b):
    assert simple_math.simple_div(a,b) == a/b

@pytest.mark.parametrize("a,b,x",[(0,1,1),(3,3,-1),(10,5,5),(-1,4,-1)])
def test_poly_first(x, a, b):
    assert simple_math.poly_first(x, a, b) == a + b*x

@pytest.mark.parametrize("a,b,c,x",[(0,1,0,1),(3,3,1,-1),(10,5,-1,5),(-1,4,10,6)])
def test_poly_second(x, a, b, c):
    assert simple_math.poly_second(x, a, b, c) == a + b*x + c*x**2