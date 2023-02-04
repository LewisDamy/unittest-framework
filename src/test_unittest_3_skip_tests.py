
#######################################################################################################
# EXERCISE 1
#######################################################################################################
'''
    The following code is given:

    Modify the implementation of the TestContainer class so that the 
    test_has_code_attribute() test is skipped, passing the reason for the skipping:
        'The Container class requires implementation.'

    Tip: Use the unittest.skip() decorator.

    You only need to modify the implementation of the TestContainer class. 
    During the solution verification, the tests are run and in case of any errors, 
    the test report will be printed to the console.
'''

import unittest


class Container:
    pass


class TestContainer_1(unittest.TestCase):

    def test_container(self):
        self.assertIsInstance(Container, type)

    @unittest.skip('The container class requires implementation')
    def test_has_code_attribute(self):
        msg = 'The Container class does not have a code attribute.'
        self.assertTrue(hasattr(Container, 'code'), msg)


#######################################################################################################
# EXERCISE 2
#######################################################################################################
'''
    The following code is given:

    Modify the implementation of the TestContainer class so that:
        - test_skipping_odd_days() method execution is skipped on odd days. 
        Provide reason for skipping test: 'Skipping odd days.'


        - test_skipping_even_days() method execution is skipped on even days. 
        Provide reason for skipping test: 'Skipping even days.'

    Tip: Use the unittest.skipIf() decorator.

    You only need to modify the implementation of the TestContainer class.
    During the solution verification, the tests are run and in case of any errors,
    the test report will be printed to the console.
'''

from datetime import date
import unittest


class Container:

    def __init__(self):
        if date.today().day % 2 == 0:
            self.code = 'XC-0'
        else:
            self.code = 'XC-1'


class TestContainer_2(unittest.TestCase):

    @unittest.skipIf(date.today().day % 2 != 0, 'Skipping odd days')
    def test_skipping_odd_days(self):
        c = Container()
        self.assertTrue(c.code.endswith('0'), 'Invalid code attribute.')

    @unittest.skipIf(date.today().day % 2 == 0, 'Skipping even days')
    def test_skipping_even_days(self):
        c = Container()
        self.assertTrue(c.code.endswith('1'), 'Invalid code attribute.')

#######################################################################################################
# EXERCISE 3
#######################################################################################################
'''
    The following code is given:

    Modify the implementation of the TestContainer class so that:

        - test_requires_windows() method only runs on Windows. 
        Provide reason for skipping test: 'Requires Windows.'

        - test_requires_linux() method only runs on Linux. 
        Provide reason for skipping test: 'Requires Linux.'

    Tip: Use the unittest.skipUnless() decorator.

    You only need to modify the implementation of the TestContainer class. 
    During the solution verification, the tests are run and in case of any errors, 
    the test report will be printed to the console.
'''

import sys
import unittest


class Container:

    def __init__(self):
        if sys.platform.startswith('win'):
            self.code = 'XC-win'
        else:
            self.code = f'XC-{sys.platform}'


class TestContainer_3(unittest.TestCase):

    @unittest.skipUnless(sys.platform.startswith('win'), 'Requires Windows')
    def test_requires_windows(self):
        c = Container()
        self.assertEqual(c.code, 'XC-win')

    @unittest.skipUnless(sys.platform.startswith('linux'), 'Requires Linux')
    def test_requires_linux(self):
        c = Container()
        self.assertEqual(c.code, 'XC-linux')