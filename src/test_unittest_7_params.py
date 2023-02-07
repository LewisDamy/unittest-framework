
#######################################################################################################
# EXERCISE 1
#######################################################################################################
'''
    In the file named tax.py the implementation of the calc_tax() function is given. 
    Create a class named TestCalcTax that inherits from unittest.TestCase and 
    implement the following four tests:

        - test_calc_tax_twenty_percent_and_eighteen_age() - checks if for arguments:
        60000, 0.2, 18 the return value is equal to 5000

        - test_calc_tax_twenty_percent_and_nineteen_age() - checks if for arguments:
        60000, 0.2, 19 the return value is equal to 12000

        - test_calc_tax_twenty_percent_and_sixty_five_age() - checks if for arguments:
        60000, 0.2, 65 the return value is equal to 12000

        - test_calc_tax_twenty_percent_and_sixty_six_age() - checks if for arguments:
        60000, 0.2, 66 the return value is equal to 8000
'''
def calc_tax_1(amount, tax_rate, age):
    """The function returns the amount of income tax."""

    if not isinstance(amount, (int, float)):
        raise TypeError('The amount value must be int or float type.')
    if not amount >= 0:
        raise ValueError('The amount value must be positive.')

    if not isinstance(tax_rate, float):
        raise TypeError('The tax_rate must be float.')
    if not 0 < tax_rate < 1:
        raise ValueError('The tax_rate must be between 0 and 1 (exclusive).')

    if not isinstance(age, int):
        raise TypeError('The age value must be int.')
    if not age > 0:
        raise ValueError('The age value must be positive.')

    if age <= 18:
        return int(min(amount * tax_rate, 5000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 8000))

import unittest

class TestCalcTax_1(unittest.TestCase):
    def test_calc_tax_twenty_percent_and_eighteen_age(self):
        self.assertEqual(calc_tax_1(60000, 0.2, 18), 5000)

    def test_calc_tax_twenty_percent_and_nineteen_age(self):
        self.assertEqual(calc_tax_1(60000, 0.2, 19), 12000)

    def test_calc_tax_twenty_percent_and_sixty_five_age(self):
        self.assertEqual(calc_tax_1(60000, 0.2, 65), 12000)

    def test_calc_tax_twenty_percent_and_sixty_six_age(self):
        self.assertEqual(calc_tax_1(60000, 0.2, 66), 8000)

#######################################################################################################
# EXERCISE 2
#######################################################################################################
'''
    In the file named tax.py the implementation of the calc_tax() function is given. 
    Try to simplify the solution of the previous exercise by using parameterized tests 
    and the unittest framework.

    Steps:
        - Implement a test method named test_calc_tax() in the TestCalcTax class.

        - In the test_calc_tax() method define four test cases (amount, tax_rate, age, result):

        (60000, 0.2, 18, 5000)
        (60000, 0.2, 19, 12000)
        (60000, 0.2, 65, 12000)
        (60000, 0.2, 66, 8000)

        - And assign to a list named cases.

        - Using the for loop and the context manager define the test cases:

        for amount, tax_rate, age, result in cases:
            with self.subTest(cases=cases):
                pass
'''

def calc_tax_2(amount, tax_rate, age):
    """The function returns the amount of income tax."""

    if not isinstance(amount, (int, float)):
        raise TypeError('The amount value must be int or float type.')
    if not amount >= 0:
        raise ValueError('The amount value must be positive.')

    if not isinstance(tax_rate, float):
        raise TypeError('The tax_rate must be float.')
    if not 0 < tax_rate < 1:
        raise ValueError('The tax_rate must be between 0 and 1 (exclusive).')

    if not isinstance(age, int):
        raise TypeError('The age value must be int.')
    if not age > 0:
        raise ValueError('The age value must be positive.')

    if age <= 18:
        return int(min(amount * tax_rate, 5000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 8000))

import unittest
# from tax import calc_tax


class TestCalcTax_2(unittest.TestCase):

    def test_calc_tax(self):
        cases = [(60000, 0.2, 18, 5000), (60000, 0.2, 19, 12000), 
                (60000, 0.2, 65, 12000), (60000, 0.2, 66, 8000)]
        
        for amount, tax_rate, age, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(calc_tax_2(amount, tax_rate, age), result)
        

#######################################################################################################
# EXERCISE 3
#######################################################################################################
'''
    The file rectangle.py implements two functions:
    - area()
    - perimeter()

    Create a class named TestArea that inherits from unittest.TestCase and implement a test
    method named test_area(). Using the parameterized tests in the created method, 
    make the following assertions:
        - check if calling the function area(1, 5) returns the value 5
        - check if calling the function area(2, 10) returns the value 20
        - check if calling the function area(100, 50) returns the value 5000
'''
def area_3(width, height):
    """The function returns the area of the rectangle."""

    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError('The width and height must be of type int or float.')

    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive.')

    return width * height

def perimeter_3(width, height):
    """The function returns the perimeter of the rectangle."""

    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError('The width and height must be of type int or float.')

    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive.')

    return 2 * width + 2 * height

#TODO

class TestArea_3(unittest.TestCase):

    def test_area(self):
        cases = [(1, 5, 5), (2, 10, 20), (100, 50, 5000)]
        for width, height, expected in cases:
            with self.subTest(cases=cases):
                self.assertEqual(area(width, height), expected)


#######################################################################################################
# EXERCISE 4
#######################################################################################################
'''
    The file rectangle.py implements two functions:
    - area()
    - perimeter()

    Add the second test method to the TestArea class named test_area_incorrect_type_should_raise_type_error(). 
    Using the parameterized tests in the created method, make the following assertions:

    - check if calling the function area(1, '5') returns TypeError

    - check if calling the function area('2', 10) returns TypeError

    - check if calling the function area('two', 'four') returns TypeError
'''
def area_4(width, height):
    """The function returns the area of the rectangle."""

    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError('The width and height must be of type int or float.')

    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive.')

    return width * height

def perimeter_4(width, height):
    """The function returns the perimeter of the rectangle."""

    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError('The width and height must be of type int or float.')

    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive.')

    return 2 * width + 2 * height

import unittest
# from rectangle import area, perimeter


class TestArea_4(unittest.TestCase):

    def test_area(self):
        cases = [
            (1, 5, 5),
            (2, 10, 20),
            (100, 50, 5000)
        ]
        for width, height, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(area_4(width, height), result)

    # enter your solution here
    def test_area_incorrect_type_should_raise_type_error(self):
        cases = [
            ('1', '5', TypeError),
            ('2', '10', TypeError),
            ('two', 'four', TypeError)
        ]
        for width, height, result in cases:
            with self.subTest(cases=cases):
                self.assertRaises(result, area, (width, height))


#######################################################################################################
# EXERCISE 5
#######################################################################################################
'''
The file rectangle.py implements two functions:
    - area()
    - perimeter()

    Add the third test method to the TestArea class named test_area_incorrect_value_should_raise_value_error(). 
    Using the parameterized tests in the created method, make the following assertions:

    - check if calling the function area(-4, 5) returns ValueError

    - check if calling the function area(4, -5) returns ValueError

    - check if calling the function area(10, 0) returns ValueError
'''
def area(width, height):
    """The function returns the area of the rectangle."""

    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError('The width and height must be of type int or float.')

    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive.')

    return width * height

def perimeter(width, height):
    """The function returns the perimeter of the rectangle."""

    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError('The width and height must be of type int or float.')

    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive.')

    return 2 * width + 2 * height

import unittest
# from rectangle import area, perimeter


class TestArea_5(unittest.TestCase):

    def test_area(self):
        cases = [
            (1, 5, 5),
            (2, 10, 20),
            (100, 50, 5000)
        ]
        for width, height, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(area(width, height), result)

    def test_area_incorrect_type_should_raise_type_error(self):
        cases = [
            (1, '5'),
            ('2', 10),
            ('two', 'four')
        ]
        for width, height in cases:
            with self.subTest(cases=cases):
                self.assertRaises(TypeError, area, width, height)

    # enter your solution here
    def test_area_incorrect_value_should_raise_value_error(self):
        cases = [
            (-4, 5),
            (4, -5),
            (10, 0)
        ]
        for width, height in cases:
            with self.subTest(cases):
                self.assertRaises(ValueError, area, width, height)


#######################################################################################################
# EXERCISE 6
#######################################################################################################
'''
    The file rectangle.py implements two functions:
    - area()
    - perimeter()

    Create a class named TestPerimeter that inherits from unittest.TestCase and implement a 
    test method named test_perimeter(). Using the parameterized tests in the created method, 
    implement the following assertions:

    - check if calling the function perimeter(1, 5) returns the value 12

    - check if calling the function perimeter(2, 10) returns the value 24

    - check if calling the function perimeter(100, 50) returns the value 300
'''
def area(width, height):
    """The function returns the area of the rectangle."""

    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError('The width and height must be of type int or float.')

    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive.')

    return width * height

def perimeter(width, height):
    """The function returns the perimeter of the rectangle."""

    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError('The width and height must be of type int or float.')

    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive.')

    return 2 * width + 2 * height

import unittest
# from rectangle import area, perimeter


class TestArea(unittest.TestCase):

    def test_area(self):
        cases = [
            (1, 5, 5),
            (2, 10, 20),
            (100, 50, 5000)
        ]
        for width, height, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(area(width, height), result)

    def test_area_incorrect_type_should_raise_type_error(self):
        cases = [
            (1, '5'),
            ('2', 10),
            ('two', 'four')
        ]
        for width, height in cases:
            with self.subTest(cases=cases):
                self.assertRaises(TypeError, area, width, height)

    def test_area_incorrect_value_should_raise_value_error(self):
        cases = [
            (-4, 5),
            (4, -5),
            (10, 0)
        ]
        for width, height in cases:
            with self.subTest(cases=cases):
                self.assertRaises(ValueError, area, width, height)


# enter your solution here
class TestPerimeter_6(unittest.TestCase):
    
    def test_perimeter(self):
        cases = [
            (1, 5, 12),
            (2, 10, 24),
            (100, 50, 300)
        ]
        for width, height, result in cases:
            with self.subTest(cases):
                self.assertEqual(perimeter(width, height), result)


#######################################################################################################
# EXERCISE 7
#######################################################################################################
'''
    The file rectangle.py implements two functions:
    - area()
    - perimeter()

    Implement a test method called test_perimeter_incorrect_type_should_raise_type_error() in 
    the TestPerimeter class. Using the parameterized tests in the created method, implement the 
    following assertions:

    - check if calling the function perimeter(4, '5') returns TypeError

    - check if calling the function perimeter('2', 8) returns TypeError

    - check if calling the function perimeter('two', 'three') returns TypeError
'''
def area(width, height):
    """The function returns the area of the rectangle."""

    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError('The width and height must be of type int or float.')

    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive.')

    return width * height

def perimeter(width, height):
    """The function returns the perimeter of the rectangle."""

    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError('The width and height must be of type int or float.')

    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive.')

    return 2 * width + 2 * height

import unittest
# from rectangle import area, perimeter


class TestArea(unittest.TestCase):

    def test_area(self):
        cases = [
            (1, 5, 5),
            (2, 10, 20),
            (100, 50, 5000)
        ]
        for width, height, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(area(width, height), result)

    def test_area_incorrect_type_should_raise_type_error(self):
        cases = [
            (1, '5'),
            ('2', 10),
            ('two', 'four')
        ]
        for width, height in cases:
            with self.subTest(cases=cases):
                self.assertRaises(TypeError, area, width, height)

    def test_area_incorrect_value_should_raise_value_error(self):
        cases = [
            (-4, 5),
            (4, -5),
            (10, 0)
        ]
        for width, height in cases:
            with self.subTest(cases=cases):
                self.assertRaises(ValueError, area, width, height)


class TestPerimeter_7(unittest.TestCase):

    def test_perimeter(self):
        cases = [
            (1, 5, 12),
            (2, 10, 24),
            (100, 50, 300)
        ]
        for width, height, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(perimeter(width, height), result)

    # enter your solution here
    def test_perimeter_incorrect_type_should_raise_type_error(self):
        cases = [
            (4, '5'),
            ('2', 8),
            ('two', 'three')
        ]
        for width, height in cases:
            with self.subTest(cases):
                self.assertRaises(TypeError, perimeter, width, height)

#######################################################################################################
# EXERCISE 8
#######################################################################################################
'''
    The file rectangle.py implements two functions:
    - area()
    - perimeter()

    Implement a test method called test_perimeter_incorrect_value_should_raise_value_error() 
    in the TestPerimeter class. Using the parameterized tests in the created method, implement 
    the following assertions:

    - check if calling the function perimeter(-40, 5) returns ValueError

    - check if calling the function perimeter(4, -10) returns ValueError

    - check if calling the function perimeter(0, 0) returns ValueError

'''
def area(width, height):
    """The function returns the area of the rectangle."""

    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError('The width and height must be of type int or float.')

    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive.')

    return width * height

def perimeter(width, height):
    """The function returns the perimeter of the rectangle."""

    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError('The width and height must be of type int or float.')

    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive.')

    return 2 * width + 2 * height

import unittest
# from rectangle import area, perimeter


class TestArea(unittest.TestCase):

    def test_area(self):
        cases = [
            (1, 5, 5),
            (2, 10, 20),
            (100, 50, 5000)
        ]
        for width, height, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(area(width, height), result)

    def test_area_incorrect_type_should_raise_type_error(self):
        cases = [
            (1, '5'),
            ('2', 10),
            ('two', 'four')
        ]
        for width, height in cases:
            with self.subTest(cases=cases):
                self.assertRaises(TypeError, area, width, height)

    def test_area_incorrect_value_should_raise_value_error(self):
        cases = [
            (-4, 5),
            (4, -5),
            (10, 0)
        ]
        for width, height in cases:
            with self.subTest(cases=cases):
                self.assertRaises(ValueError, area, width, height)


class TestPerimeter_8(unittest.TestCase):

    def test_perimeter(self):
        cases = [
            (1, 5, 12),
            (2, 10, 24),
            (100, 50, 300)
        ]
        for width, height, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(perimeter(width, height), result)

    def test_perimeter_incorrect_type_should_raise_type_error(self):
        cases = [
            (4, '5'),
            ('2', 8),
            ('two', 'three')
        ]
        for width, height in cases:
            with self.subTest(cases=cases):
                self.assertRaises(TypeError, perimeter, width, height)

    # enter your solution here
    def test_perimeter_incorrect_value_should_raise_value_error(self):
        cases = [
            (-40, 5),
            (4, -10),
            (0, 0)
        ]
        for width, height in cases:
            with self.subTest(cases):
                self.assertRaises(ValueError, perimeter, width, height)

