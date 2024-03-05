"""
A collection of simple math operations
"""

def simple_add(a,b):
    """
    Return the sum of two numbers.
    Parameters
    ----------
    a : integer, float
    The value of the first number
    b : integer, float
    The value of the second number

    Returns
    -------
    c : integer, float
    The sum of the numbers.
    Examples
    --------
    >>> simple_math.simple_add(3,2)
    5
    >>> simple_math.simple_add(5,-4)
    1
    """
    return a+b

def simple_sub(a,b):
    """
    Returns the value of a subtracted by b.
    Parameters
    ----------
    a : integer, float
    The value of the first number
    b : integer, float
    The value of the number to be subtracted

    Returns
    -------
    c : integer, float
    The value of a subtracted by b
    Examples
    --------
    >>> simple_math.simple_sub(35,210)
    25
    >>> simple_math.simple_add(10,-4)
    14
    """
    
    return a-b

def simple_mult(a,b):
    """
    Return the product of two numbers.
    Parameters
    ----------
    a : integer, float
    The value of the first number
    b : integer, float
    The value of the second number

    Returns
    -------
    c : integer, float
    The product of the numbers.
    Examples
    --------
    >>> simple_math.simple_mul(3,2)
    6
    >>> simple_math.simple_mul(5,-4)
    -20
    """
    return a*b

def simple_div(a,b):
    """
    Return the value of the first number divided by second number.
    Parameters
    ----------
    a : integer, float
    The value of the first number
    b : integer, float
    The value of the second number

    Returns
    -------
    c : integer, float
    The value of the division.
    Examples
    --------
    >>> simple_math.simple_div(3,2)
    1.5
    >>> simple_math.simple_div(8,2)
    4
    """
    
    return a/b

def poly_first(x, a0, a1):
    """
    Return the value of first order polynomial given the location (x),
    the fixed term and the slope of the straight line.
    Parameters
    ----------
    x : integer, float
    Coordinate at which the value of the polynome must be evaluated
    a0 : integer, float
    Fixed term of the straight line
    a1 : integer, float
    Slope of the straight line

    Returns
    -------
    c : integer, float
    Value of the polynomial at x for a line characterized by coefficients a0 and a1.
    Examples
    --------
    >>> simple_math.poly_first(0,3,2)
    3
    >>> simple_math.poly_first(1.5, 5,-4)
    -1
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    Return the value of second order polynomial given the location (x),
    and the coefficients of the polynomial.
    Parameters
    ----------
    x : integer, float
    Coordinate at which the value of the polynome must be evaluated
    a0 : integer, float
    Fixed term of the straight line
    a1 : integer, float
    First-order coefficient
    a2 : integer, float
    Second-order coefficient
    Returns
    -------
    c : integer, float
    Value of the polynomial at x for a line characterized by coefficients a0, a1 and a2.
    Examples
    --------
    >>> simple_math.poly_first(0,3,2,5)
    3
    >>> simple_math.poly_first(2, 5,-4, 5)
    17
    """
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
