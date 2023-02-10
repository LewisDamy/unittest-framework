
#######################################################################################################
# EXERCISE 1
#######################################################################################################
'''
    Tests for the map_longest() function are implemented in a file named exercise.py. The 
    implementation of this function should be in a file named solution.py. Your task is to 
    complete the implementation of this function in solution.py so that it passes the tests 
    implemented in exercise.py.

    How map_longest() works:

    The function takes a list of words (no validation) and returns the length of the longest word in a 
    list. If an empty list is passed, it returns 0.

    Example:
        [IN]: map_longest(['python', 'sql'])
        [OUT]: 6

        [IN]: map_longest(['java', 'sql', 'r'])
        [OUT]: 4
'''

def map_longest(words:list) -> int:
    # my answer:
    counter = 0
    for item in words:
        if counter < len(item):
            counter = len(item)
    return counter
    # sample solution answer:
    if not words:
        return 0
    lengths = []
    for word in words:
        lengths.append(len(word))
    return max(lenghts)


import unittest
# from solution import map_longest

class TestMapLongest(unittest.TestCase):

    def test_map_longest_should_be_six(self):
        msg = 'Correct the implementation of the map_longest() function.'
        self.assertEqual(map_longest(['sql', 'r', 'python']), 6, msg)

    def test_map_longest_should_be_three(self):
        msg = 'Correct the implementation of the map_longest() function.'
        self.assertEqual(map_longest(['sql', 'r']), 3, msg)

    def test_map_longest_should_be_zero(self):
        msg = 'Correct the implementation of the map_longest() function.'
        self.assertEqual(map_longest([]), 0, msg)


#######################################################################################################
# EXERCISE 2
#######################################################################################################
'''
    Tests for the filter_ge_four_char() function are implemented in a file named exercise.py. The 
    implementation of this function should be in a file named solution.py. Your task is to complete 
    the implementation of this function in solution.py so that it passes the tests implemented in 
    exercise.py.

    How filter_ge_four_char() works:

    The function takes a list of words (no validation) and returns a list of words that are exactly 
    four characters or more.

    Example:
        [IN]: filter_ge_four_char(['programm', 'python', 'sql'])
        [OUT]: ['programm', 'python']


        [IN]: filter_ge_four_char(['c++', 'sql'])
        [OUT]: []
'''

def filter_ge_four_char(words:list) -> list:
    # my response:
    output = []
    for word in words:
        if len(word) >= 4:
            output.append(word)
    return output


import unittest
# from solution import filter_ge_four_char


class TestFilterGeFourChar(unittest.TestCase):

    def test_filter_ge_four_char_with_one_item(self):
        msg = 'Correct the implementation of the filter_ge_four_char() function.'
        actual = filter_ge_four_char(['sql', 'r', 'java'])
        expected = ['java']
        self.assertEqual(actual, expected, msg)

    def test_filter_ge_four_char_with_two_item(self):
        msg = 'Correct the implementation of the filter_ge_four_char() function.'
        actual = filter_ge_four_char(['sql', 'r', 'python', 'java'])
        expected = ['python', 'java']
        self.assertEqual(actual, expected, msg)

    def test_filter_ge_four_char_should_be_empty(self):
        msg = 'Correct the implementation of the filter_ge_four_char() function.'
        actual = filter_ge_four_char([])
        expected = []
        self.assertEqual(actual, expected, msg)


#######################################################################################################
# EXERCISE 3
#######################################################################################################
'''
    Tests for the factorial() function are implemented in a file named exercise.py. The implementation 
    of this function should be in a file named solution.py. Your task is to complete the implementation 
    of this function in solution.py so that it passes the tests implemented in exercise.py.

    How factorial() works:

    The function takes a non-negative integer and returns the factorial of that number. You do not need 
    to implement validation of the argument passed to the function.


    Tip: Use recursion.

    Example:
        [IN]: factorial(6)
        [OUT]: 720

        [IN]: factorial(10)
        [OUT]: 3628800
'''

def factorial(n:int) -> int:
    if n == 0:
        return 1
    else:
        return n*factorial(n - 1)


import unittest
# from solution import factorial


class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        msg = 'Correct the implementation of factorial() function.'
        self.assertEqual(factorial(0), 1, msg)
        self.assertEqual(factorial(1), 1, msg)
        self.assertEqual(factorial(2), 2, msg)
        self.assertEqual(factorial(3), 6, msg)
        self.assertEqual(factorial(6), 720, msg)


#######################################################################################################
# EXERCISE 4
#######################################################################################################
'''
    Tests for the count_string() function are implemented in a file named exercise.py. The 
    implementation of this function should be in a file named solution.py. Your task is to 
    complete the implementation of this function in solution.py so that it passes the tests 
    implemented in exercise.py.

    How count_string() works:

    The function takes a list (without validation) and returns the number of elements of type 
    str present in the list.

    Example:
        [IN]: count_string(['p', 2, 4.3, None])
        [OUT]: 1


        [IN]: count_string({'p', 2, 4.3, True, 'True', None})
        [OUT]: 2
'''

def count_string(items:list) -> int:
    result = 0
    for item in items:
        if type(item) == str:
        # if isintance(item, str):
            result += 1
    return result



import unittest
# from solution import count_string


class TestCountString(unittest.TestCase):

    def test_count_string_empty_list(self):
        msg = 'Correct the implementation of the count_string() function.'
        self.assertEqual(count_string([]), 0, msg)

    def test_count_string_without_string(self):
        msg = 'Correct the implementation of the count_string() function.'
        self.assertEqual(count_string([1, 2]), 0, msg)

    def test_count_string_with_three_string(self):
        msg = 'Correct the implementation of the count_string() function.'
        self.assertEqual(count_string(['c++', 3, 'c', 'java']), 3, msg)


#######################################################################################################
# EXERCISE 5
#######################################################################################################
'''
    Tests for the remove_duplicates() function are implemented in a file named exercise.py. The 
    implementation of this function should be in a file named solution.py. Your task is to 
    complete the implementation of this function in solution.py so that it passes the tests 
    implemented in exercise.py.

    How remove_duplicates() works:

    The function takes a list (no validation), removes duplicates, and returns the 
    list with no duplicates.

    Example:
        [IN]: remove_duplicates([1, 5, 3, 2, 2, 4, 2, 4])
        [OUT]: [1, 2, 3, 4, 5]

        [IN]: remove_duplicates([1, 1, 1, 1])
        [OUT]: [1]
'''

def remove_duplicates(items:list) -> list:
    # my result
    result = []
    for item in items:
        if item not in result:
            result.append(item) 
    if all([isinstance(item, int) for item in result]):
        result.sort()
    return result
    # sample result
    return list(set(items))

import unittest
# from solution import remove_duplicates


class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates_empty_list(self):
        msg = 'Correct the implementation of the remove_duplicates() function.'
        self.assertEqual(remove_duplicates([]), [], msg)

    def test_remove_duplicates_without_string(self):
        msg = 'Correct the implementation of the remove_duplicates() function.'
        self.assertEqual(remove_duplicates([3, 3, 1]), [1, 3], msg)

    def test_remove_duplicates_with_three_string(self):
        msg = 'Correct the implementation of the remove_duplicates() function.'
        actual = sorted(remove_duplicates(['c++', 'c', 'c']))
        expected = ['c', 'c++']
        self.assertEqual(actual, expected, msg)


#######################################################################################################
# EXERCISE 6
#######################################################################################################
'''
    Tests for the is_distinct() function are implemented in a file named exercise.py. The 
    implementation of this function should be in a file named solution.py. Your task is to 
    complete the implementation of this function in solution.py so that it passes the tests 
    implemented in exercise.py.

    How is_distinct() works:

    The function takes a list (no validation) and returns True if the list contains no duplicates, 
    returns False otherwise.

    Example:
        [IN]: is_distinct([1, 2, 3])
        [OUT]: True


        [IN]: is_distinct([1, 2, 3, 3])
        [OUT]: False
'''

def is_distinct(items: list) -> bool:
    arr_true = []
    for item in items:
        if item not in arr_true:
            arr_true.append(item)
        else:
            return False
    return True
    # sample solution
    return len(items) == len(set(items))


import unittest
# from solution import is_distinct


class TestIsDistinct(unittest.TestCase):

    def test_is_distinct_empty_list(self):
        msg = 'Correct the implementation of the is_distinct() function.'
        self.assertEqual(is_distinct([]), True, msg)

    def test_is_distinct_with_numbers_should_return_false(self):
        msg = 'Correct the implementation of the is_distinct() function.'
        self.assertEqual(is_distinct([3, 3, 1]), False, msg)

    def test_is_distinct_with_numbers_should_return_true(self):
        msg = 'Correct the implementation of the is_distinct() function.'
        self.assertEqual(is_distinct([3, 2, 1]), True, msg)

    def test_is_distinct_with_strings(self):
        msg = 'Correct the implementation of the is_distinct() function.'
        self.assertEqual(is_distinct(['c++', 'c', 'r']), True, msg)

#######################################################################################################
# EXERCISE 7
#######################################################################################################
'''
    Tests for the Phone class are in a file named exercise.py. The implementation of this class 
    should be in a file named solution.py. Your task is to complete the implementation of this 
    class in solution.py so that it passes the tests implemented in exercise.py.

    The Phone class should have two user-defined class attributes named appropriately:

    - brand
    - model

    You can set the values of these attributes freely, e.g.
        brand = 'Apple'
        model = 'iPhone X'
'''

class Phone:
    @classmethod
    def brand(self, brand):
        self.brand = brand
    
    @classmethod
    def model(self, model):
        self.model = model


import unittest
# from solution import Phone


class TestPhone(unittest.TestCase):

    def test_brand_attr(self):
        msg = 'The brand attribute for the Phone class is missing.'
        self.assertTrue(hasattr(Phone, 'brand'), msg)

    def test_model_attr(self):
        msg = 'The model attribute for the Phone class is missing.'
        self.assertTrue(hasattr(Phone, 'model'), msg)

    def test_check_user_defined_class_attr(self):
        msg = 'Two Phone class attributes are not defined.'
        actual = len([attr for attr in dir(Phone) if not attr.startswith('_')])
        expected = 2
        self.assertEqual(actual, expected, msg)


#######################################################################################################
# EXERCISE 8
#######################################################################################################
'''
    Tests for the Laptop class are in a file named exercise.py. The implementation of this class should 
    be in a file named solution.py. Your task is to complete the implementation of this class in 
    solution.py so that it passes the tests implemented in exercise.py.

    The Laptop class in the __init__() method should set three instance attributes 
    (without validation) with the names:
        - brand
        - model
        - price
'''

class Laptop_8:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


import unittest
# from solution import Laptop


class TestLaptop_8(unittest.TestCase):

    def setUp(self):
        self.laptop = Laptop_8('Acer', 'Predator', 5490)

    def test_laptop_has_brand_instance_attr(self):
        msg = 'brand instance attribute is missing.'
        self.assertTrue(hasattr(self.laptop, 'brand'), msg)

    def test_laptop_has_model_instance_attr(self):
        msg = 'model instance attribute is missing.'
        self.assertTrue(hasattr(self.laptop, 'model'), msg)

    def test_laptop_has_price_instance_attr(self):
        msg = 'price instance attribute is missing.'
        self.assertTrue(hasattr(self.laptop, 'price'), msg)

    def test_laptop_has_three_instance_attrs(self):
        msg = 'Three instance attributes are not defined.'
        actual = len([attr for attr in dir(self.laptop)
                      if not attr.startswith('_')])
        expected = 3
        self.assertEqual(actual, expected, msg)


#######################################################################################################
# EXERCISE 9
#######################################################################################################
'''
    Tests for the Laptop class are in a file named exercise.py.

    The Laptop class in the __init__() method sets three instance attributes 
    (without validation) with the names:
    - brand
    - model
    - price

    Your task is to fix the Laptop implementation in solution.py to pass the tests implemented in 
    exercise.py. Add validation for an instance attribute named price. If the value passed is of type 
    int or float set the value of this attribute, otherwise raise a TypeError.
'''

class Laptop_9:

    def __init__(self, brand:str, model:str, price):
        self.brand = brand
        self.model = model
        if not isinstance(price, (int, float)):
            raise TypeError
        else:
            self.price = price


import unittest
# from solution import Laptop


class TestLaptop_9(unittest.TestCase):

    def test_laptop_incorrect_price_should_raise_type_error(self):
        self.assertRaises(TypeError, Laptop_9, 'Acer', 'Predator', 'thousand')
        self.assertRaises(TypeError, Laptop_9, 'Acer', 'Predator', [2000])
        self.assertRaises(TypeError, Laptop_9, 'Acer', 'Predator', None)


#######################################################################################################
# EXERCISE 10
#######################################################################################################
'''
    Tests for the Laptop class are in a file named exercise.py.

    The Laptop class in the __init__() method sets three instance attributes with names:
    - brand
    - model
    - price

    Your task is to fix the Laptop implementation in solution.py to pass the tests implemented in 
    exercise.py. Add another validation for an instance attribute named price. If the passed value 
    is positive set the value of this attribute, otherwise raise ValueError.
'''

class Laptop_10:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        if not isinstance(price, (int, float)):
            raise TypeError('The price attribute must be a positive int or float.')
        if not price > 0:
            raise ValueError
        self.price = price



import unittest
# from solution import Laptop


class TestLaptop_10(unittest.TestCase):

    def test_laptop_incorrect_price_should_raise_type_error(self):
        self.assertRaises(TypeError, Laptop_10, 'Acer', 'Predator', 'thousand')
        self.assertRaises(TypeError, Laptop_10, 'Acer', 'Predator', [2000])
        self.assertRaises(TypeError, Laptop_10, 'Acer', 'Predator', None)

    def test_laptop_incorrect_price_should_raise_value_error(self):
        self.assertRaises(ValueError, Laptop_10, 'Acer', 'Predator', -1000)
        self.assertRaises(ValueError, Laptop_10, 'Acer', 'Predator', 0)


#######################################################################################################
# EXERCISE 11
#######################################################################################################
'''
    Tests for the Laptop class are in a file named exercise.py.

    The Laptop class in the __init__() method sets three instance attributes with names:
    - brand
    - model
    - price

    Your task is to fix the Laptop implementation in solution.py to pass the tests implemented in 
    exercise.py. Add validation for an instance attribute named brand. If the value passed is an 
    object of type str set the value of this attribute, otherwise raise a TypeError.
'''
class Laptop_11:

    def __init__(self, brand, model, price):
        if not isinstance(brand, str):
            raise TypeError
        self.brand = brand
        self.model = model
        if not isinstance(price, (int, float)):
            raise TypeError('The price attribute must be a positive int or float.')
        if not price > 0:
            raise ValueError('The price attribute must be positive.')
        self.price = price


import unittest
# from solution import Laptop


class TestLaptop_11(unittest.TestCase):

    def test_laptop_incorrect_brand_should_raise_type_error(self):
        self.assertRaises(TypeError, Laptop_11, 200, 'Predator', 1000)
        self.assertRaises(TypeError, Laptop_11, True, 'Predator', 1000)

    def test_laptop_incorrect_price_should_raise_type_error(self):
        self.assertRaises(TypeError, Laptop_11, 'Acer', 'Predator', 'thousand')
        self.assertRaises(TypeError, Laptop_11, 'Acer', 'Predator', [2000])
        self.assertRaises(TypeError, Laptop_11, 'Acer', 'Predator', None)

    def test_laptop_incorrect_price_should_raise_value_error(self):
        self.assertRaises(ValueError, Laptop_11, 'Acer', 'Predator', -1000)
        self.assertRaises(ValueError, Laptop_11, 'Acer', 'Predator', 0)



#######################################################################################################
# EXERCISE 12
#######################################################################################################
'''
    Tests for the Pet class are in a file named exercise.py. Your task is to fix the Pet 
    implementation in solution.py so that it passes the tests implemented in exercise.py.

    Implement a method named name() that returns the value of the protected attribute _name. 
    Then use the @property decorator to create a property with the same name as method 
    (a read-only property).
'''

class Pet_12:

    def __init__(self, name):
        self._name = name

    # enter your solution here
    @property
    def name(self):
        return self._name


import unittest
# from solution import Pet


class TestPet_12(unittest.TestCase):

    def test_pet_has_name_property(self):
        msg = 'The Pet class does not have a name attribute.'
        self.assertTrue(hasattr(Pet_12, 'name'), msg)
        self.assertIsInstance(Pet_12.name, property)


#######################################################################################################
# EXERCISE 13
#######################################################################################################
'''
    Tests for the Pet class are in a file named exercise.py. Your task is to fix the Pet 
    implementation in solution.py so that it passes the tests implemented in exercise.py.

    Implement a method named age() that returns the value of the protected attribute _age. 
    Then use the @property decorator to create a property with the same name as 
    method (a read-only property).
'''
class Pet_13:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    # enter your solution her
    @property
    def age(self):
        return self._age

import unittest
# from solution import Pet


class TestPet_13(unittest.TestCase):

    def test_pet_has_name_property(self):
        msg = 'The Pet class does not have a name attribute.'
        self.assertTrue(hasattr(Pet_13, 'name'), msg)
        self.assertIsInstance(Pet_13.name, property)

    def test_pet_has_age_property(self):
        msg = 'The Pet class does not have an age attribute.'
        self.assertTrue(hasattr(Pet_13, 'age'), msg)
        self.assertIsInstance(Pet_13.age, property)


#######################################################################################################
# EXERCISE 14
#######################################################################################################
'''
    Tests for the Person class are in a file named exercise.py. Your task is to fix the Person 
    implementation in solution.py so that it passes the tests implemented in exercise.py.

    Implement a special method named __repr__() that is a formal representation of an object 
    of Person class.

    Example:
        [IN]: person = Person('John', 'Doe')
        [IN]: print(person)
        [OUT]: Person(fname='John', lname='Doe')
'''
class Person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


    def __repr__(self):
        return f"Person(fname='{self.fname}', lname='{self.lname}')"

import unittest
# from solution import Person


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person('John', 'Smith')

    def test_person_repr_method(self):
        msg = 'Correct the implementation of the __repr__() method.'
        actual = repr(self.person)
        expected = "Person(fname='John', lname='Smith')"
        self.assertEqual(actual, expected, msg)


#######################################################################################################
# EXERCISE 15
#######################################################################################################
'''
    Tests for the Vector class are in a file named exercise.py. Your task is to fix the Vector 
    implementation in solution.py so that it passes the tests implemented in exercise.py.

    Implement a special method named __repr__() that is a formal representation of an 
    object of Vector class.

    Example:
        [IN]: v1 = Vector(3, 4, 5)
        [IN]: print(v1)
        [Out]: Vector(3, 4, 5)
'''

class Vector_15:

    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'


import unittest
# from solution import Vector


class TestVector_15(unittest.TestCase):

    def setUp(self):
        self.v = Vector_15(-3, 4, 2)

    def test_vector_repr_method(self):
        msg = 'Correct the implementation of the __repr__() method.'
        actual = repr(self.v)
        expected = "Vector(-3, 4, 2)"
        self.assertEqual(actual, expected, msg)


#######################################################################################################
# EXERCISE 16
#######################################################################################################
'''
    Tests for the Vector class are in a file named exercise.py. Your task is to fix the Vector 
    implementation in solution.py so that it passes the tests implemented in exercise.py.

    Implement a special method called __len__() that will return the length of a 
    Vector (number of coordinates).

    Example:
        [IN]: v1 = Vector(3, 4, 5)  
        [IN]: print(len(v1))
        [Out]: 3
'''

class Vector_16:

    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'

    def __len__(self):
        return len(self.components)

import unittest
# from solution import Vector


class TestVector_16(unittest.TestCase):

    def setUp(self):
        self.v = Vector_16(-3, 4, 2)
        self.w = Vector_16(1, -3)

    def test_vector_repr_method(self):
        msg = 'Correct the implementation of the __repr__() method.'
        self.assertEqual(repr(self.v), "Vector(-3, 4, 2)", msg)
        self.assertEqual(repr(self.w), "Vector(1, -3)", msg)

    def test_vector_len_method(self):
        msg = 'Correct the implementation of the __len__() method.'
        self.assertEqual(len(self.v), 3, msg)
        self.assertEqual(len(self.w), 2, msg)