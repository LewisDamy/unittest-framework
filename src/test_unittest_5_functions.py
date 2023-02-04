
#######################################################################################################
# EXERCISE 1
#######################################################################################################
'''
    The following area() function is given (calculates the area of a circle with a given radius):

    Implement the TestArea class inheriting from the unittest.TestCase class and 
    implementing further tests:

    - test_circle_area_with_radius_one() - test verifying the correctness of calculating 
    the circle area with radius=1 (compare the result to the 5th decimal place)

    - test_circle_area_with_radius_three() - test verifying the correctness of calculating 
    the area of a circle with radius=3 (compare the result to 5 decimal place)

    - test_area_incorrect_type_should_raise_type_error()
        checks if the call area('4') returns TypeError
        checks if the call area(None) returns TypeError

    - test_area_incorrect_value_should_raise_value_error()
        checks if the call area(0) returns ValueError
        checks if the call area(-3) returns ValueError

    You only need to implement the class and the appropriate test methods. During the solution 
    verification, the tests are run and in case of any errors, the test report will be printed 
    to the console.
'''

import unittest
import math


def area(radius):
    """The function returns the area of the circle."""

    if not (isinstance(radius, (int, float))):
        raise TypeError('The radius must be of type int or float.')

    if not radius > 0:
        raise ValueError('The radius must be positive.')

    return math.pi * radius ** 2
    

# enter your solution here


#######################################################################################################
# EXERCISE 2
#######################################################################################################
'''
    The following perimeter() function is given (calculates the length of a circle with a given radius).

    Implement the TestPerimeter class inheriting from the unittest.TestCase class and 
    implementing four different tests. Choose any tests you like. Use several different 
    assertion methods.

    You only need to implement the class and test methods. During the solution verification, 
    the tests are run and in case of any errors, the test report will be printed to the console.
'''

import unittest
import math


def perimeter(radius):
    """The function returns the length of the circle."""

    if not (isinstance(radius, (int, float))):
        raise TypeError('The radius must be of type int or float.')

    if not radius > 0:
        raise ValueError('The radius must be positive.')

    return 2 * math.pi * radius


# enter your solution here



#######################################################################################################
# EXERCISE 3
#######################################################################################################
'''
    An implementation of the following calculate_tax() function is given in the tax.py file:

    The calculate_tax() function was imported into exercise.py file (solution). 
    
    Create a TestCalculateTax class that inherits from unittest.TestCase and 
    implements the following tests:

        - test_tax_with_eighteen_age() checks if for the amount of 60,000 and 
        the age of 18, the calculated tax will be 6,000


        - test_tax_with_nineteen_age() checks if for the amount of 60,000 and 
        the age of 19, the calculated tax will be 10,200


        - test_tax_with_sixty_five_age() checks if for the amount of 60,000 and 
        the age of 65, the calculated tax will be 10,200


        - test_tax_with_sixty_six_age() checks if for the amount of 60,000 and 
        the age of 66, the calculated tax will be 9,000

    Use the default income tax rate of 17%.

    You only need to implement the class and the appropriate test methods. 
    During the solution verification, the tests are run and in case of any errors, 
    the test report will be printed to the console.

'''

import unittest
# from tax import calculate_tax

def calculate_tax(amount, age, tax=17.0):
    """The function returns the amount of income tax."""
 
    tax_rate = tax / 100.0
 
    if age <= 18:
        return int(min(amount * tax_rate, 6000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 9000))


# enter your solution here

#######################################################################################################
# EXERCISE 4
#######################################################################################################
'''
    The following calculate_tax() function in a file tax.py is given:

    Import calculate_tax() function from the tax module into the exercise.py file. 
    Create a TestCalculateTax class that inherits from unittest.TestCase and implements 
    the following tests:

        - test_tax_twenty_percent_with_eighteen_age() checks if for the amount of 
        60,000 and the age of 18, the calculated tax will be 6,000


        - test_tax_twenty_percent_with_nineteen_age() checks if for the amount of 
        60,000 and the age of 19, the calculated tax will be 12,000


        - test_tax_twenty_percent_with_sixty_five_age() checks if for the amount of
        60,000 and the age of 65, the calculated tax will be 12,000


        - test_tax_twenty_percent_with_sixty_six_age() checks if for the amount of 
        60,000 and the age of 66, the calculated tax will be 9,000

    Apply a 20% income tax rate.

    You only need to implement the class and the appropriate test methods. During the solution 
    verification, the tests are run and in case of any errors, the test report will be 
    printed to the console.
'''
import unittest

def calculate_tax(amount, age, tax=17.0):
    """The function returns the amount of income tax."""
    tax_rate = tax / 100.0
 
    if age <= 18:
        return int(min(amount * tax_rate, 6000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 9000))

# enter your solution here



#######################################################################################################
# EXERCISE 5
#######################################################################################################
'''
    The following implementation of the income_tax() function is given in the tax.py file:

    Import the function income_tax() from the tax module into exercise.py file. 
    Create a TestIncomeTax class that inherits from the unittest.TestCase class and 
    implements the following tests:

        - test_tax_below_threshold() checks if the calculated tax for 
        the amount of 60,000 will be 10,200


        - test_tax_equal_threshold() checks if the calculated tax for 
        the amount 85,528 will be 14,539.76


        - test_tax_above_threshold() checks if the calculated tax for 
        the amount 100,000 will be 19,170.8

    You only need to implement the class and the appropriate test methods. 
    During the solution verification, the tests are run and in case of any errors, 
    the test report will be printed to the console.
'''
import unittest

def income_tax(income, first_thresh=17.0, second_thresh=32.0):
    first_rate = first_thresh / 100.0
    second_rate = second_thresh / 100.0
    threshold = 85528
    if income < threshold:
        return income * first_rate
    else:
        return threshold * first_rate + (income - threshold) * second_rate

# enter your solution here