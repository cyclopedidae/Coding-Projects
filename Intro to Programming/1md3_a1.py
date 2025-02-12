import math
g = 9.81
pi = math.pi

def is_a_number(s:str)-> bool:
    """
    Returns True if and only if s is a string representing a positive number.

    Examples:
    >>> is_a_number("1")
    True
    >>> is_a_number("One")
    False
    >>> is_a_number("-3")
    False
    >>> is_a_number("3.")
    True
    >>> is_a_number("3.1.2")
    False
    """
    #Your code goes here
    try:
        float(s)
    except:
        return False
    else:
        if float(s) > 0:
            return True
        else:
            return False