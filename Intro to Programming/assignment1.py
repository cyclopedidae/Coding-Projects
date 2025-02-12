import math
g = 9.81
pi = math.pi

def get_distance(velocity:float, angle:float)-> float:
    """
    Calculates the distance a projectile travels on a flat surface
    given its intial velocity, as well as the angle of fire relative
    to the x-axis. The angle is given in radian. This function assumes
    perfect physics, i.e., constant gravity, no air resistance, etc.

    >>> get_distance(0, 1)
    0.0
    >>> get_distance(1, 0)
    0.0
    >>> get_distance(10, 0.25*pi)
    10.19367991845056
    """
    #Your code goes here

    distance = (pow(velocity, 2)*sin(angle*2))/g


def degrees_to_radians(d:float)-> float:
    """
    Takes in an angle in degrees, d, and returns an equivalent
    angle in radians

    >>> degrees_to_radians(0)
    0.0
    >>> degrees_to_radians(180)
    3.141592653589793
    """
    #Your code goes here


def get_radian_of(angle_string: str)-> float:
    """
    Takes in a valid input angle_str and returns the numerical value of the
    angle in radians.

    Examples:
    >>> get_radian_of("1.2r")
    1.2
    >>> get_radian_of("1.2R")
    1.2
    >>> get_radian_of("45d")
    0.7853981633974483
     >>> get_radian_of("45D")
    0.7853981633974483
    """
    #Your code goes here


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

    

def is_valid_angle(s:str)-> bool:
    """
    Returns True if and only if s is a valid angle. See the assignment
    description and examples for more information regarding what's valid

    Examples:
    >>> is_valid_angle("85.3d")
    True
    >>> is_valid_angle("85.3.7D")
    False
    >>> is_valid_angle("90d")
    False
    >>> is_valid_angle("0.001r")
    True
    >>> is_valid_angle("1.5R")
    True
    """
    #Your code goes here

    s = s.lower()

    if s.isdigit() ==  True: 
        return False #Doesn't have angle (letter), so invalid
    elif s.rfind("d") >= 1:
        if 90 > float(s.replace("d", "")) > 0:
            return True
    elif s.endswith("r"):
        if (pi/2) > float(s.replace("r", "")) > 0:
            return True


def approx_equal(x, y, tol):
    """
    Returns True if and only if x and y are within tol of each other.

    Examples:
    >>> approx_equal(1,2,1)
    True
    >>> approx_equal(4,3,1)
    True
    >>> approx_equal(4,3,0.99)
    False
    >>> approx_equal(-1.5,1.5,3)
    True
    """
    #Your code goes here
    if abs(x - y) == tol:
        return True
    else:
        return False


"""
DO NOT MODIFY THE CODE BELOW.

You are not required/expected to understand the following code.
If you're interested though, take a look.
"""
if __name__ == "__main__":
    while True:
        target = float(input("Enter a target distance: "))
        tol = float(input("Enter how close you need to be to your target: "))
        target_hit = False
        while not target_hit:
            valid_velocity = False
            while not valid_velocity:
                v = input("Enter a valid velocity: ")
                valid_velocity = is_a_number(v)   
            valid_angle = False
            v = float(v)
            while not valid_angle:
                theta = input("Enter a valid angle: ")
                valid_angle = is_valid_angle(theta)
            theta = get_radian_of(theta)
            d = get_distance(float(v), theta)
            target_hit = approx_equal(target, d, tol)
            if target_hit:
                print("Congratulations! You hit the target.")
            elif target > d:
                print("The shot hit short of the target, try again.")
            else: 
                print("The shot hit past the target, try again.")
            
                
