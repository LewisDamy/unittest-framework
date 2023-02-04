#######################################################################################################
# EXERCISE 1
#######################################################################################################
'''
    The following calculate_daily_return() function is given, which takes two arguments: open and close 
    (open and close price of a financial instrument from a trading session). The function returns the 
    value of the daily rate of return (in percent).

    Complete the implementation of the TestCalculateDailyReturn  class by adding three test methods:

    test_positive_return()
    - using the method assertEqual check if code
    - calculate_daily_return(349.0, 360.0) returns the daily rate of return 3.15

    test_negative_return()
    - using the method assertEqual check if code
    - calculate_daily_return(349.0, 340.0) returns the daily rate of return -2.58


    test_zero_return()
    - using the method assertEqual check if code
    - calculate_daily_return(349.0, 349.0) returns the daily rate of return 0.0

    You only need to implement test methods. During the solution verification, the tests are run 
    and in case of any errors, the test report will be printed to the console.
'''

import unittest


def calculate_daily_return(open, close):
    return round((close / open - 1) * 100, 2)


class TestCalculateDailyReturn(unittest.TestCase):
    def test_positive_return(self):
        actual = calculate_daily_return(349.0, 360.0)
        self.assertEqual(actual, 3.15)

    def test_negative_return(self):
        actual = calculate_daily_return(349.0, 340.0)
        self.assertEqual(actual, -2.58)
    
    def test_zero_return(self):
        actual = calculate_daily_return(349.0, 349.0)
        self.assertEqual(actual, 0.0)



    #######################################################################################################
    # EXERCISE 2
    #######################################################################################################
'''
    The following calculate_daily_return() function is given, which takes two arguments: open and close
    (open and close price of a financial instrument from a trading session). The function returns the 
    value of the daily rate of return.

    Complete the implementation of the TestCalculateDailyReturn class by adding three test methods:

    test_positive_return()
    using the method assertAlmostEqual  check if code calculate_daily_return(349.0, 360.0) returns 
    the appropriate value


    test_negative_return()
    using the method assertAlmostEqual check if code calculate_daily_return(349.0, 340.0) returns 
    the appropriate value


    test_zero_return()
    using the method assertAlmostEqual check if code calculate_daily_return(349.0, 349.0) returns 
    the appropriate value

    Note: Note how the assertAlmostEqual method works.

    You only need to implement test methods. During the solution verification, the tests are run 
    and in case of any errors, the test report will be printed to the console.
'''

import unittest


def calculate_daily_return(open, close):
    return (close / open - 1) * 100


class TestCalculateDailyReturn(unittest.TestCase):
    def test_postive_return(self):
        actual = calculate_daily_return(349.0, 360.0)
        self.assertAlmostEqual(actual, 3.1518625)
    
    def test_negative_return(self):
        actual = calculate_daily_return(349.0, 340.0)
        self.assertAlmostEqual(actual, -2.5787966)
    
    def test_zero_return(self):
        actual = calculate_daily_return(349.0, 349.0)
        self.assertAlmostEqual(actual, 0)





#######################################################################################################
# EXERCISE 3
#######################################################################################################
'''
    The following Doc class is given:
    
    Using the unittest framework create a TestDoc class that inherits from the 
    unittest.TestCase class that implements two test methods:

    test_less_than()
    checks if doc2 < doc1 - use the assertLess() method for this purpose
    checks if doc3 < doc1 - use the assertLess() method for this purpose


    test_greater_than()
    checks if doc1 > doc2 - use the assertGreater() method for this purpose
    checks if doc1 > doc3 - use the assertGreater() method for this purpose

    Where doc1, doc2, doc3 are instances of Doc class, respectively:
    doc1 = Doc('Technology')
    doc2 = Doc('Online')
    doc3 = Doc('Nature')

    You only need to implement the class and the appropriate test methods. During the solution 
    verification, the tests are run and in case of any errors, the test report will be printed
    to the console.
'''

import unittest


class Doc:

    def __init__(self, string):
        self.string = string
        
    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __lt__(self, other):
        return len(self.string) < len(other.string)


# enter your solution here
class TestDoc(unittest.TestCase):
    def test_less_than(self):
        doc1 = Doc('Technology')
        doc2 = Doc('Online')
        doc3 = Doc('Nature')
        self.assertLess(doc2, doc1)
        self.assertLess(doc3, doc1)
 
    def test_greater_than(self):
        doc1 = Doc('Technology')
        doc2 = Doc('Online')
        doc3 = Doc('Nature')
        self.assertGreater(doc1, doc2)
        self.assertGreater(doc1, doc3)



#######################################################################################################
# EXERCISE 4
#######################################################################################################
'''
    The following Doc class is given:

    Using the unittest framework create a TestDoc class that inherits from the unittest.TestCase class 
    that implements two test methods:

    test_equal()
    checks if doc1 == doc2 use the assertEqual() method for this purpose


    test_not_equal()
    checks if doc3 != doc1 use the assertNotEqual() method for this purpose
    checks if doc3 != doc2 use the assertNotEqual() method for this purpose

    Where doc1, doc2, doc3 are instances of Doc class, respectively:
    doc1 = Doc('Online')
    doc2 = Doc('Nature')
    doc3 = Doc('Technology')

    You only need to implement the class and the appropriate test methods. During the solution 
    verification, the tests are run and in case of any errors, the test report will be printed to the console.
'''

import unittest


class Doc:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __eq__(self, other=Doc):    
        return len(self.string) == len(other.string)


# enter your solution here
class TestDoc(unittest.TestCase):
    def test_equal(self):
        doc1 = Doc('Online')
        doc2 = Doc('Nature')
        doc3 = Doc('Technology')
        self.assertEqual(doc1, doc2)
    
    
    def test_not_equal(self):
        doc1 = Doc('Online')
        doc2 = Doc('Nature')
        doc3 = Doc('Technology')
        self.assertNotEqual(doc3, doc1)
        self.assertNotEqual(doc3, doc2)


#######################################################################################################
# EXERCISE 5
#######################################################################################################
'''
    The implementation of the Employee class is given:

    Using the unittest framework create a TestEmployee class that inherits from 
    the unittest.TestCase class that implements three test methods:

    test_has_email_attr()

    checks whether the Employee class has the attribute email, if the attribute is missing, 
    return the message:
        'The Employee class does not have an email attribute.'


    test_has_tax_attr()
    checks whether the Employee class has the attribute tax, if the attribute is missing, return the message:
        'The Employee class does not have a tax attribute.'


    test_has_apply_bonus()
    checks whether the Employee class has the attribute apply_bonus, if the attribute is
    missing, return the message:
        'The Employee class does not have an apply_bonus attribute.'

    Tip: Use the built-in function hasattr() and the assertTrue() assertion method.

    You only need to implement the class and the appropriate test methods. During the solution 
    verification, the tests are run and in case of any errors, the test report will be printed to the console.
'''

import unittest

'''
class Employee:
    """A simple class that describes an employee of the company."""

    tax_rate = 0.17
    bonus_rate = 0.10

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@mail.com'

    @property
    def tax(self):
        return round(self.salary * self.tax_rate, 2)

    def apply_bonus(self):
        self.salary = int(self.salary * (1 + self.bonus_rate))


# enter your solution here
class TestEmployee(unittest.TestCase):
    def test_has_email_attr(self):
        msg = 'The Employee class does not have an email attribute.'
        self.assertTrue(hasattr(Employee, 'email'), msg)

    def test_has_tax_attr(self):
        msg = 'The Employee class does not have a tax attribute.'
        self.assertTrue(hasattr(Employee, 'tax'), msg)

    def test_has_apply_bonus(self):
        msg = 'The Employee class does not have an apply_bonus attribute.'
        self.assertTrue(hasattr(Employee, 'apply_bonus'), msg)
'''


#######################################################################################################
# EXERCISE 6
#######################################################################################################
'''
    The implementation of the Employee class is given:

    Using the unittest framework create a TestEmployee class that inherits from the unittest.TestCase class
    that implements two test methods:

    test_has_email_attr()
    checks whether the Employee class has the attribute email, if the attribute is missing, 
    return the message:
        'The Employee class does not have an email attribute.'


    test_has_email_property()
    checks if the email attribute of the Employee class is of the type property. Use the 
    assertIsInstance() method for this purpose.

    You only need to implement the class and the appropriate test methods. During the solution
    verification, the tests are run and in case of any errors, the test report will be printed to the console.
'''

import unittest


class Employee:
    """A simple class that describes an employee of the company."""

    tax_rate = 0.17
    bonus_rate = 0.10

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def email(self):
        return (
            f'{self.first_name.lower()}.{self.last_name.lower()}'
            '@mail.com'
        )

    @property
    def tax(self):
        return round(self.salary * self.tax_rate, 2)

    def apply_bonus(self):
        self.salary = int(self.salary * (1 + self.bonus_rate))


# enter your solution here
class TestEmployee(unittest.TestCase):
    def test_has_email_attr(self):
        msg = 'The Employee class does not have an email attribute.'
        self.assertTrue(hasattr(Employee, 'email'), msg)

    def test_has_email_property(self):
        self.assertIsInstance(Employee.email, property)



#######################################################################################################
# EXERCISE 7
#######################################################################################################
'''
    An implementation of the StringListOnly class is given:

    Only objects of type str can be added to the list of type StringListOnly using the append() 
    method.

    Using the unittest framework create a TestStringListOnly class that inherits from the 
    unittest.TestCase class that implements two test methods:

    test_append_string()
    checks if we can add an object of the str type to the StringListOnly instance using the 
    append() method. Use the assertIn() method for this purpose.


    test_append_not_string_should_raise_error()
    - checks if TypeError is raised when trying to add an instance of type list. To do this, use the 
    assertRaises() method.
    - checks if TypeError is raised when trying to add an instance of type bool. To do this, use 
    the assertRaises() method.

    You only need to implement the class and the appropriate test methods. During the solution 
    verification, the tests are run and in case of any errors, the test report will be printed to 
    the console.
'''

import unittest


class StringListOnly(list):
    def append(self, string):
        if not isinstance(string, str):
            raise TypeError('Only object of type str can be added to the list.')
        super().append(string)


# enter your solution here
class TestStringListOnly(unittest.TestCase):
    def test_append_string(self):
        myStringListInstance = StringListOnly()
        string = 'coding_skills'
        myStringListInstance.append(string)
        self.assertIn(string, myStringListInstance)

    def test_append_not_string_should_raise_error(self):
        myStringListInstance = StringListOnly()
        myListString = ['coding_skills']
        myBooleanValue = True
        # self.assertRaises(ERROR, FunctionCallable, argsFunc)
        self.assertRaises(TypeError, myStringListInstance.append, myListString) 
        self.assertRaises(TypeError, myStringListInstance.append, myBooleanValue)



#######################################################################################################
# EXERCISE 8
#######################################################################################################
'''
    An implementation of the StringListOnly class is given:

    Only objects of type str can be added to the list of type StringListOnly using the 
    append() method.

    Using the unittest framework create a TestStringListOnly class that inherits from the 
    unittest.TestCase class that implements the test method:

    test_slo_is_instance()
    - checks if instance slo = StringListOnly() is an instance of the StringListOnly class. 
    Use the assertIsInstance() method.
    - checks if instance slo = StringListOnly() is an instance of the list class. Use the 
    assertIsInstance() method.

    You only need to implement the class and the appropriate test methods. During the solution 
    verification, the tests are run and in case of any errors, the test report will be printed 
    to the console.
'''

import unittest


class StringListOnly(list):

    def append(self, string):
        if not isinstance(string, str):
            raise TypeError('Only object of type str can be added to the list.')
        super().append(string)


# enter your solution here
class TestStringListOnly(unittest.TestCase):
    def test_slo_is_instance(self):
        slo = StringListOnly()
        self.assertIsInstance(slo, StringListOnly)
        self.assertIsInstance(slo, list)