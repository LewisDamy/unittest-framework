
#######################################################################################################
# EXERCISE 1
#######################################################################################################
'''
    Using the unittest framework, create a TestSplitMethod class that inherits from the unittest.
    TestCase class and implements the following three tests:

    test_split_by_default()

    test that checks if the code 'Python Testing'.split() returns a list
    ['Python', 'Testing']

    test_split_by_comma()

    test that checks if the code 'open,high,low,close'.split(',') returns a list ['open', 'high', 'low', 'close']

    test_split_by_hash()

    test that checks if the code 'summer#time#vibes'.split('#') returns a list ['summer', 'time', 'vibes']

    You only need to define the class and the appropriate tests. During the solution verification, 
    the tests are run and in case of any errors, the test report will be printed to the console.
'''
import unittest


# enter your solution here
class TestSplitMethod(unittest.TestCase):
    def test_split_by_default(self):
        self.assertEqual('Python Testing'.split(), ['Python', 'Testing'])

    def test_split_by_comma(self):
        actual = 'open,high,low,close'.split(',')
        expected = ['open', 'high', 'low', 'close']
        self.assertEqual(actual, expected)
    
    def test_split_by_hash(self):
        actual = 'summer#time#vibes'.split('#')
        expected = ['summer', 'time', 'vibes']
        self.assertEqual(actual, expected)


#######################################################################################################
# EXERCISE 2
#######################################################################################################
'''
    Using the unittest framework, create a TestJoinMethod class that inherits from the unittest.TestCase class
    and implements the following three tests:

    test_join_with_space()

    test that checks if the code ' '.join(['Python', '3.8']) returns a list
    'Python 3.8'

    test_join_with_comma()

    test that checks if the code ','.join(['open', 'high', 'low', 'close']) returns a list 'open,high,low,close'

    test_join_with_new_line_char()

    test that checks if the code '\n'.join(['open', 'high', 'low', 'close']) returns a list 'open\nhigh\nlow\nclose'

    You only need to define the class and the appropriate tests. During the solution verification, 
    the tests are run and in case of any errors, the test report will be printed to the console.

'''

import unittest


# enter your solution here
class TestJoinMethod(unittest.TestCase):
    def test_join_with_space(self):
        self.assertEqual(' '.join(['Python', '3.8']), 'Python 3.8')

    def test_join_with_comma(self):
        actual = ','.join(['open', 'high', 'low', 'close'])
        expected = 'open,high,low,close'
        self.assertEqual(actual, expected)

    def test_join_with_new_line_char(self):
        actual = '\n'.join(['open', 'high', 'low', 'close'])
        expected = 'open\nhigh\nlow\nclose'
        self.assertEqual(actual, expected)


#######################################################################################################
# EXERCISE 3
#######################################################################################################
'''
    Using the unittest framework, the TestJoinMethod class was created. The class has the following three tests:

    test_join_with_space()

    test that checks if the code ' '.join(['Python', '3.8']) returns a list
    'Python 3.8'

    test_join_with_comma()

    test that checks if the code ','.join(['open', 'high', 'low', 'close']) returns a list 'open,high,low,close'


    test_join_with_new_line_char()

    test that checks if the code '\n'.join(['open', 'high', 'low', 'close']) returns a list 'open\nhigh\nlow\nclose'

    First, run all tests (check the solution by clicking the 'Check solution' button). 
    Pay attention to the result. One of the tests was written incorrectly. 
    Try to correct it and run the tests again.
'''

import unittest

class TestJoinMethod(unittest.TestCase):

    def test_join_with_space(self):
        self.assertEqual(' '.join(['Python', '3.8']), 'Python 3.8')
        pass

    def test_join_with_comma(self):
        actual = ','.join(['open', 'high', 'low', 'close'])
        expected = 'open,high,low,close'
        self.assertEqual(actual, expected)

    def test_join_with_new_line_char(self):
        actual = '\n'.join(['open', 'high', 'low', 'close'])
        expected = 'open\nhigh\nlow\nclose'
        self.assertEqual(actual, expected)


#######################################################################################################
# EXERCISE 4
#######################################################################################################
'''
    The following TestIsInstance class is given:

    Add one more test named test_case_6() that checks the type of var2 (note the comma after the number 4):

    var2 = 4,

    Then run all tests.
'''

import unittest
from collections import Counter

class TestIsInstance(unittest.TestCase):

    def test_case_1(self):
        self.assertTrue(isinstance((), tuple))

    def test_case_2(self):
        self.assertTrue(isinstance([], list))

    def test_case_3(self):
        self.assertTrue(isinstance({}, dict))

    def test_case_4(self):
        cnt = Counter()
        self.assertTrue(isinstance(cnt, Counter))

    def test_case_5(self):
        var1 = 4
        self.assertTrue(isinstance(var1, int))

    # enter your solution here
    def test_case_6(self):
        var2 = 4,
        self.assertTrue(isinstance(var2, tuple))


#######################################################################################################
# EXERCISE 5
#######################################################################################################
'''
    Using the unittest framework create a TestUpper class that inherits from the unittest.TestCase class
    and implements the following two tests:

    test_upper()

    test that checks if the code  'summer'.upper() returns string 'SUMMER'

    test_is_upper()

    test that checks if the code 'SUMMER'.isupper() returns the boolean value True
    test that checks if the code 'summer'.isupper() returns the boolean value False

    You only need to define the class and the appropriate tests. During the solution verification, 
    the tests are run and in case of any errors, the test report will be printed to the console.

'''

import unittest


# enter your solution here
class TestUpper(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('summer'.upper(), 'SUMMER')

    def test_is_upper(self):
        self.assertTrue('SUMMER'.isupper())
        self.assertFalse('summer'.isupper())


#######################################################################################################
# EXERCISE 6
#######################################################################################################
'''
    Using the unittest framework create a TestLower class that inherits from the unittest.TestCase class
    and implements the following two tests:

    test_lower()

    test that checks if the code 'Joe.Smith@mail.com'.lower() returns string 'joe.smith@mail.com'

    test_is_lower()

    test that checks if the code 'joe.smith@mail.com'.islower() returns the boolean value True
    test that checks if the code 'Joe.Smith@mail.com'.islower() returns the boolean value False

    You only need to define the class and the appropriate tests. During the solution verification, 
    the tests are run and in case of any errors, the test report will be printed to the console.
'''

import unittest


# enter your solution here
class TestLower(unittest.TestCase):
    def test_lower(self):
        actual = 'Joe.Smith@mail.com'.lower()
        expected = 'joe.smith@mail.com'
        self.assertEqual(actual, expected)
    
    def test_is_lower(self):
        case1 = 'joe.smith@mail.com'.islower()
        case2 = 'Joe.Smith@mail.com'.islower()
        self.assertTrue(case1)
        self.assertFalse(case2)


#######################################################################################################
# EXERCISE 7
#######################################################################################################
'''
    Using the unittest framework create two classes named: TestStartswithMethod and TestEndswithMethod 
    that inherit from the unittest.TestCase class.

    The TestStartswithMethod class implements two test methods:

    test_startswith_one_letter()

    test that checks if the code 'unittest'.startswith('u') returns the boolean value True
    test that checks if the code 'unittest'.startswith('U') returns the boolean value False


    test_startswith_four_letters()

    test that checks if the code 'http://www.e-smartdata.org/'.startswith('http') returns the boolean value True
    test that checks if the code 'www.e-smartdata.org/'.startswith('http') returns the boolean value False

    The TestEndswithMethod class implements one test method:

    test_endswith_three_letter()

    test that checks if the code 'e-smartdata.org'.endswith('org') returns the boolean value True
    test that checks if the code 'e-smartdata.org'.endswith('com') returns the boolean value False

    You only need to define classes and the appropriate test methods. During the solution verification, 
    the tests are run and in case of any errors, the test report will be printed to the console.

''' 

import unittest


# enter your solution here
class TestStartswithMethod(unittest.TestCase):
    def test_startswith_one_letter(self):
        self.assertTrue('unittest'.startswith('u'))
        self.assertFalse('unittest'.startswith('U'))

    def test_startswith_four_letters(self):
        self.assertTrue('http://www.e-smartdata.org'.startswith('http'))
        self.assertFalse('www.e-smartdadta.org/'.startswith('http'))

class TestEndswithMethod(unittest.TestCase):
    def test_endswith_three_letter(self):
        self.assertTrue('e-smartdata.org'.endswith('org'))
        self.assertFalse('e-smartdata.org'.endswith('com'))

#######################################################################################################
# EXERCISE 8
#######################################################################################################
'''
    Using the unittest framework create three classes named: TestLstripMethod, TestStripMethod and 
    TestRstripMethod that inherit from the unittest.TestCase class. Then add two test methods to each class, 
    testing the behavior of the methods appropriately:

    str.lstrip()
    str.strip()
    str.rstrip()

    Select the names of the test methods and test cases as you see fit.
'''

import unittest


# enter your solution here
class TestLstripMethod(unittest.TestCase):
    def test_lstrip_with_space(self):
        self.assertEqual('  price,volume  '.lstrip(), 'price,volume  ')

    def test_lstrip_with_new_line_char(self):
        self.assertEqual('\nprice,volume\n'.lstrip(), 'price,volume\n')

class TestStripMethod(unittest.TestCase):
    def test_strip_with_space(self):
        self.assertEqual('  price,volume  '.strip(), 'price,volume')
 
    def test_strip_with_new_line_char(self):
        self.assertEqual('\nprice,volume\n'.strip(), 'price,volume')

class TestRstripMethod(unittest.TestCase):
    def test_rstrip_with_space(self):
        self.assertEqual('  price,volume  '.rstrip(), '  price,volume')
 
    def test_rstrip_with_new_line_char(self):
        self.assertEqual('\nprice,volume\n'.rstrip(), '\nprice,volume')

