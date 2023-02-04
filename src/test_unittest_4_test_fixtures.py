
#######################################################################################################
# EXERCISE 1
#######################################################################################################
'''
    The following code is given:

    Note that we use the same piece of code in each test:
        container = Container()

    Try to replace these two pieces of code by adding the setUpModule() function, 
    which will create a Container instance named container at the level of the 
    entire test module. The container instance should be reachable from within each test.

    Tip: Use the global statement.

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


class TestContainer(unittest.TestCase):
    @unittest.skipUnless(
        sys.platform.startswith('win'), 'Requires Windows.'
    )
    def test_requires_windows(self):
        container = Container()  # code to remove
        self.assertEqual(container.code, 'XC-win')

    @unittest.skipUnless(
        sys.platform.startswith('linux'), 'Requires Linux.'
    )
    def test_requires_linux(self):
        container = Container()  # code to remove
        self.assertEqual(container.code, 'XC-linux')



# enter your solution here


#######################################################################################################
# EXERCISE 2
#######################################################################################################
'''
    The following code is given:

    Add a function called tearDownModule() that will allow you to remove the container 
    instance after testing is complete.

    Tip: Use the global statement.

    During the solution verification, the tests are run and in case of any errors, the 
    test report will be printed to the console.    
'''

import sys
import unittest


class Container:
    
    def __init__(self):
        if sys.platform.startswith('win'):
            self.code = 'XC-win'
        else:
            self.code = f'XC-{sys.platform}'


class TestContainer(unittest.TestCase):
    
    @unittest.skipUnless(
        sys.platform.startswith('win'), 'Requires Windows.'
    )
    def test_requires_windows(self):
        self.assertEqual(container.code, 'XC-win')

    @unittest.skipUnless(
        sys.platform.startswith('linux'), 'Requires Linux.'
    )
    def test_requires_linux(self):
        self.assertEqual(container.code, 'XC-linux')


def setUpModule():
    global container
    container = Container()

    
# enter your solution here



#######################################################################################################
# EXERCISE 3
#######################################################################################################
'''
    The following code is given:

    Note that we use the same piece of code in each test:
        container = Container()

    Try to override these two pieces of code by adding a class method called setUpClass() 
    of TestContainer class, which will allow you to create a Container instance at the 
    level of the entire test class (as an attribute of the TestContainer class) named container.

    During the solution verification, the tests are run and in case of any errors, the 
    test report will be printed to the console.
'''

import sys
import unittest


class Container:
    
    def __init__(self):
        if sys.platform.startswith('win'):
            self.code = 'XC-win'
        else:
            self.code = f'XC-{sys.platform}'


class TestContainer(unittest.TestCase):

    # enter your solution here

    @unittest.skipUnless(
        sys.platform.startswith('win'), 'Requires Windows.'
    )
    def test_requires_windows(self):
        container = Container()  # code to remove
        self.assertEqual(
            container.code, 'XC-win'
        )  # code to modify

    @unittest.skipUnless(
        sys.platform.startswith('linux'), 'Requires Linux.'
    )
    def test_requires_linux(self):
        container = Container()  # code to remove
        self.assertEqual(
            container.code, 'XC-linux'
        )  # code to modify



#######################################################################################################
# EXERCISE 4
#######################################################################################################
'''
    The following code is given:

    Add a class method named tearDownClass() to remove the container attribute of 
    TestContainer (after performing all tests in this class.)

    During the solution verification, the tests are run and in case of any errors, the 
    test report will be printed to the console.
'''

import sys
import unittest


class Container:
    
    def __init__(self):
        if sys.platform.startswith('win'):
            self.code = 'XC-win'
        else:
            self.code = f'XC-{sys.platform}'


class TestContainer(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.container = Container()

    # enter your solution here

    @unittest.skipUnless(
        sys.platform.startswith('win'), 'Requires Windows.'
    )
    def test_requires_windows(self):
        self.assertEqual(self.container.code, 'XC-win')

    @unittest.skipUnless(
        sys.platform.startswith('linux'), 'Requires Linux.'
    )
    def test_requires_linux(self):
        self.assertEqual(self.container.code, 'XC-linux')



#######################################################################################################
# EXERCISE 5
#######################################################################################################
'''
    The following code is given:

    Note that we use the same piece of code in each test:
        container = Container('plastic')

    Try to replace these two pieces of code by adding a method called setUp() of the 
    TestContainer class, which will allow you to create an instance of the Container 
    class at the level of each test (as an attribute of the TestContainer class) 
    named container.

    During the solution verification, the tests are run and in case of any errors, 
    the test report will be printed to the console.
'''

import sys
import unittest


class Container:
    
    def __init__(self, category):
        self.category = category

    def __repr__(self):
        return f"Container(category='{self.category}')"


class TestContainer(unittest.TestCase):

    # enter your solution here

    def test_init_method(self):
        container = Container('plastic')  # remove this
        msg = (
            'The container instance does not have a category '
            'attribute.'
        )
        self.assertTrue(
            hasattr(container, 'category'), msg
        )  # modify this
        self.assertEqual(
            container.category, 'plastic'
        )  # modify this

    def test_repr_method(self):
        container = Container('plastic')  # remove this
        self.assertEqual(
            repr(container), "Container(category='plastic')"
        )  # modify this



#######################################################################################################
# EXERCISE 6
#######################################################################################################
'''
    The following code is given:

    Add a method named tearDown() to remove the container attribute of TestContainer class 
    after each test.

    During the solution verification, the tests are run and in case of any errors, the test 
    report will be printed to the console.
'''

import sys
import unittest


class Container:
    
    def __init__(self, category):
        self.category = category

    def __repr__(self):
        return f"Container(category='{self.category}')"


class TestContainer(unittest.TestCase):
    
    def setUp(self):
        self.container = Container('plastic')

    # enter your solution here

    def test_init_method(self):
        msg = (
            'The container instance does not have a category '
            'attribute.'
        )
        self.assertTrue(hasattr(self.container, 'category'), msg)
        self.assertEqual(self.container.category, 'plastic')

    def test_repr_method(self):
        self.assertEqual(
            repr(self.container), "Container(category='plastic')"
        )
