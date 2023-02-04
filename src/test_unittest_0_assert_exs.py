#######################################################################################################
# EXERCISE 1
#######################################################################################################
'''
    Assert the is_italy variable using the assert statment
'''

countries = ['POL', 'ENG', 'GER', 'USA', 'ITA']
is_italy = 'ITA' in countries

# enter your solution here
assert is_italy

#######################################################################################################
# EXERCISE 2
#######################################################################################################
'''
    Assert the is_canada variable using the assert statement:

    countries = ['POL', 'ENG', 'GER', 'USA', 'ITA']
    is_canada = 'CAN' in countries

    Expected Action: Raising AssertionError.
'''

countries = ['POL', 'ENG', 'GER', 'USA', 'ITA']
is_canada = 'CAN' in countries

# enter your solution here
# try:
assert is_canada == False
# except:
#     raise AssertionError

#######################################################################################################
# EXERCISE 3
#######################################################################################################
'''
    The implementation of the max_min_diff() function is given:

    def max_min_diff(numbers):
        return max(numbers) - min(numbers)

    Modify the implementation of the max_min_diff() function. By using the assert statement inside this function, add the ability to check the length of the numbers argument before returning the result. If the length of the numbers object is 0 raise the AssertionError without any message. Otherwise, return the correct result.

    In response call max_min_diff() function passing an empty list.
'''
def max_min_diff(numbers):
    # enter your solution here
    if len(numbers) == 0:
        raise AssertionError
    else:
        result = max(numbers) - min(numbers)
        return result

    max_min_diff([])


#######################################################################################################
# EXERCISE 4
#######################################################################################################
'''
    The implementation of the max_min_diff() function is given:

    def max_min_diff(numbers):
        return max(numbers) - min(numbers)

    Modify the implementation of the max_min_diff() function. By using the assert statement inside this function, add the ability to check the length of the numbers argument before returning the result. If the length of the numbers object is 0 raise the AssertionError with message:

    'The numbers object cannot be empty.'

    Otherwise, it returns the correct result (the difference between the highest and lowest value for numbers).

    In case the module with the solution is run directly, call the max_min_diff() function passing an empty list.

    Tip: Use the conditional statement and the module's __name__ attribute for this:

    if __name__ == '__main__':
        do_something()
'''
def max_min_diff(numbers):
    # enter your solution here
    assert len(numbers) != 0, 'The numbers object cannot be empty.'
    return max(numbers) - min(numbers)
 
 
# if __name__ == '__main__':
    max_min_diff([])

#######################################################################################################
# EXERCISE 5
#######################################################################################################
'''
    The following area() function is given, which returns the area of a rectangle (no argument validation).

    def area(width, height):
        return width * height

    Assert the following function calls:
    area(4, 10)
    area(5, 6)

    with the appropriate values:
    40
    30
'''
def area(width, height):
    return width * height

# enter your solution here
assert area(4, 10) == 40
assert area(5, 6) == 30

#######################################################################################################
# EXERCISE 6
#######################################################################################################
'''
    The following area() function is given, which returns the area of a rectangle with additional argument validation:

    Assert the following function call:

    area('5', '4')

    with a value of 20.

    Expected Action: Raising TypeError.
'''

def area(width, height):
    """The function returns the area of the rectangle."""

    if not (isinstance(width, int) and isinstance(height, int)):
        raise TypeError(
            'The width and height must be of type int.'
        )
    if not (width > 0 and height > 0):
        raise ValueError(
            'The width and height must be positive.'
        )
    return width * height


# enter your solution here
# try: -> already happens
assert area(5, 4) == 20
# except:
    # raise TypeError -> already happens



#######################################################################################################
# EXERCISE 7
#######################################################################################################
'''
The following area() function is given which returns the area of a rectangle.

Assert the following function call:

area(-4, 5)

with a value of 20. Note that the first argument is negative.

Expected Action: Raising ValueError.
'''

def area(width, height):
    """The function returns the area of the rectangle."""

    if not (isinstance(width, int) and isinstance(height, int)):
        raise TypeError(
            'The width and height must be of type int.'
        )

    if not (width > 0 and height > 0):
        raise ValueError(
            'The width and height must be positive.'
        )

    return width * height

# enter your solution here
    assert area(-4, 5)

#######################################################################################################
# EXERCISE 8    
#######################################################################################################
'''
    The calculate_tax() function is given (no argument validation):\

    Implement a function called test_calculate_tax() that asserts the following test cases:

    calculate_tax(60000, 0.15, 10) == 5000

    calculate_tax(60000, 0.15, 18) == 5000

    calculate_tax(60000, 0.15, 19) == 9000

    calculate_tax(60000, 0.15, 65) == 9000

    calculate_tax(60000, 0.15, 66) == 8000

    Then call test_calculate_tax() function.
'''

def calculate_tax(amount, tax_rate, age):
    """The function returns the amount of income tax."""

    if age <= 18:
        return int(min(amount * tax_rate, 5000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 8000))

# enter your solution here
def test_calculate_tax():
    assert calculate_tax(60000, 0.15, 10) == 5000

    assert calculate_tax(60000, 0.15, 18) == 5000

    assert calculate_tax(60000, 0.15, 19) == 9000

    assert calculate_tax(60000, 0.15, 65) == 9000

    assert calculate_tax(60000, 0.15, 66) == 8000




#######################################################################################################
# EXERCISE 9
#######################################################################################################
'''
    The calculate_tax() function is given (no argument validation):

    The function is supposed to work as follows:

    for age 18 or under, returns the minimum of the following two values:
        amount * tax_rate
        5000

    for age over 18 and age less than or equal to 65 returns:
        amount * tax_rate

    for the age over 65, it returns a minimum of the following two values:
        amount * tax_rate
        8000

    There are two bugs in the calculate_tax() function implementation. 
    Try to correct these bugs so that the function passes the tests implemented in the test_calculate_tax() function.

    The test_calculate_tax() function asserts the following test cases:
        calculate_tax(60000, 0.15, 10) == 5000
        calculate_tax(60000, 0.15, 18) == 5000
        calculate_tax(60000, 0.15, 19) == 9000
        calculate_tax(60000, 0.15, 65) == 9000
        calculate_tax(60000, 0.15, 66) == 8000
'''

def calculate_tax(amount, tax_rate, age):
    """The function returns the amount of income tax."""

    if age <= 18:
        return int(min(amount * tax_rate, 5000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 8000))

def test_calculate_tax():
    assert calculate_tax(60000, 0.15, 10) == 5000        
    assert calculate_tax(60000, 0.15, 18) == 5000
    assert calculate_tax(60000, 0.15, 19) == 9000
    assert calculate_tax(60000, 0.15, 65) == 9000
    assert calculate_tax(60000, 0.15, 66) == 8000


