
#######################################################################################################
# EXERCISE 1
#######################################################################################################
'''
    The implementation of the SimpleTaxCalculator class is given in the tax.py file. 
    Import the SimpleTaxCalculator class from the tax module into the exercise.py file. 
    Next, create a TestIncomeTax class that inherits from unittest.TestCase. Add the setUpClass() 
    method to create an instance of the SimpleTaxCalculator class and assign it to the attribute 
    named calc of the TestIncomeTax class.

    Test the income_tax() method of the SimpleTaxCalculator class. To do this implement the 
    following test methods in the TestIncomeTax class:
        - test_income_below_threshold() checks if the calculated tax for income=60000 is equal to 10200

        - test_income_equal_threshold() checks if the calculated tax of income=85528 is equal to 14539.76

        - test_income_above_threshold() checks if the calculated tax of income=100000 is equal to 19170.8
'''
import unittest

class SimpleTaxCalculator_1:

    def income_tax(self, income, first_thresh=17.0, second_thresh=32.0):
        first_rate = first_thresh / 100.0
        second_rate = second_thresh / 100.0
        threshold = 85528
        if income < threshold:
            return income * first_rate
        else:
            return threshold * first_rate + (income - threshold) * second_rate

    def vat_tax(self, net_price, tax=23.0):
        tax_rate = tax / 100.0
        return net_price * tax_rate

    def capital_gains_tax(self, profit, tax=19.0):
        tax_rate = tax / 100.0
        if profit > 0:
            return profit * tax_rate
        return 0


# enter your solution here
class TestIncomeTax_1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = SimpleTaxCalculator()

    def test_income_below_threshold(self):
        actual = self.calc.income_tax(income=60000)
        self.assertEqual(actual, 10200)

    def test_income_equal_threshold(self):
        actual = self.calc.income_tax(income=85528)
        self.assertEqual(actual, 14539.76)

    def test_income_above_threshold(self):
        actual = self.calc.income_tax(income=100000)
        self.assertEqual(actual, 19170.8)

#######################################################################################################
# EXERCISE 2
#######################################################################################################
'''
    The implementation of the SimpleTaxCalculator class is given in the tax.py file. Add the 
    TestVatTax class that inherits from the unittest.TestCase class to the exercise.py file. 
    Also add the setUpClass() method to create an instance of the SimpleTaxCalculator class 
    and assign it to an attribute named calc of the TestVatTax class.

    Test the vat_tax() method of the SimpleTaxCalculator class. To do this implement the following 
    test methods in the TestVatTax class:
        - test_vat_tax_with_default() checks if the calculated tax for net_price=100 is equal to 23.0

        - test_vat_tax_with_twenty_tax_rate() checks if the calculated tax for net_price=100 and 
        tax=20.0 is equal to 20.0
'''

class SimpleTaxCalculator:

    def income_tax(self, income, first_thresh=17.0, second_thresh=32.0):
        first_rate = first_thresh / 100.0
        second_rate = second_thresh / 100.0
        threshold = 85528
        if income < threshold:
            return income * first_rate
        else:
            return threshold * first_rate + (income - threshold) * second_rate

    def vat_tax(self, net_price, tax=23.0):
        tax_rate = tax / 100.0
        return net_price * tax_rate

    def capital_gains_tax(self, profit, tax=19.0):
        tax_rate = tax / 100.0
        if profit > 0:
            return profit * tax_rate
        return 0


import unittest
# from tax import SimpleTaxCalculator


class TestIncomeTax(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calc = SimpleTaxCalculator()

    def test_income_below_threshold(self):
        self.assertEqual(self.calc.income_tax(60000), 10200)

    def test_income_equal_threshold(self):
        self.assertEqual(self.calc.income_tax(85528), 14539.76)

    def test_income_above_threshold(self):
        self.assertEqual(self.calc.income_tax(100000), 19170.8)


# enter your solution here
class TestVatTax_1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.calc = SimpleTaxCalculator()

    def test_vat_tax_with_default(self):
        actual = self.calc.vat_tax(net_price=100)
        self.assertEqual(actual, 23.0)

    def test_vat_tax_with_twenty_tax_rate(self):
        actual = self.calc.vat_tax(net_price=100, tax=20.0)
        self.assertEqual(actual, 20.0)


#######################################################################################################
# EXERCISE 3
#######################################################################################################
'''
    The implementation of the SimpleTaxCalculator class is given in the tax.py file. Add the 
    TestCapitalGainsTax class that inherits from the unittest.TestCase class to the exercise.py file. 
    Add the setUpClass() method to create a SimpleTaxCalculator instance and assign it to an attribute 
    named calc of TestCapitalGainsTax.

    Test the capital_gains_tax() method of the SimpleTaxCalculator class. To do this implement the 
    following test methods in the TestCapitalGainsTax class:

        - test_positive_profit() checks if the calculated tax for profit=1000 is equal to 190.0

        - test_zero_profit() checks if the calculated tax for profit=0 is equal to 0.0

        - test_negative_profit() checks if the calculated for profit=-1000 is equal to 0.0
'''
class SimpleTaxCalculator:

    def income_tax(self, income, first_thresh=17.0, second_thresh=32.0):
        first_rate = first_thresh / 100.0
        second_rate = second_thresh / 100.0
        threshold = 85528
        if income < threshold:
            return income * first_rate
        else:
            return threshold * first_rate + (income - threshold) * second_rate

    def vat_tax(self, net_price, tax=23.0):
        tax_rate = tax / 100.0
        return net_price * tax_rate

    def capital_gains_tax(self, profit, tax=19.0):
        tax_rate = tax / 100.0
        if profit > 0:
            return profit * tax_rate
        return 0

import unittest
# from tax import SimpleTaxCalculator


class TestIncomeTax(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calc = SimpleTaxCalculator()

    def test_income_below_threshold(self):
        self.assertEqual(self.calc.income_tax(60000), 10200)

    def test_income_equal_threshold(self):
        self.assertEqual(self.calc.income_tax(85528), 14539.76)

    def test_income_above_threshold(self):
        self.assertEqual(self.calc.income_tax(100000), 19170.8)


class TestVatTax(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calc = SimpleTaxCalculator()

    def test_vat_tax_with_default(self):
        self.assertEqual(self.calc.vat_tax(100), 23.0)

    def test_vat_tax_with_twenty_tax_rate(self):
        self.assertEqual(self.calc.vat_tax(100, 20.0), 20.0)


# tutaj wpisz rozwiązanie        
class TestCapitalGainsTax_1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.calc = SimpleTaxCalculator()

    def test_positive_profit(self):
        actual = self.calc.capital_gains_tax(profit=1000)
        self.assertEqual(actual, 190.0)
    
    def test_zero_profit(self):
        actual = self.calc.capital_gains_tax(profit=0)
        self.assertEqual(actual, 0.0)
    
    def test_negative_profit(self):
        actual = self.calc.capital_gains_tax(profit=-1000)
        self.assertEqual(actual, 0.0)



#######################################################################################################
# EXERCISE 4
#######################################################################################################
'''
    The implementation of the SimpleTaxCalculator class is given in the tax.py file. There are 
    three test classes in exercise.py:
    - IncomeTaxTest
    - VatTaxTest
    - CapitalGainsTaxTest

    Each of these classes implements a class method named setUpClass() that performs the same 
    operation in each test class. Modify the solution to replace these three class methods with a 
    single module-level function named setUpModule() that creates a SimpleTaxCalculator class 
    instance named calc that is globally available.
'''
class SimpleTaxCalculator:

    def income_tax(self, income, first_thresh=17.0, second_thresh=32.0):
        first_rate = first_thresh / 100.0
        second_rate = second_thresh / 100.0
        threshold = 85528
        if income < threshold:
            return income * first_rate
        else:
            return threshold * first_rate + (income - threshold) * second_rate

    def vat_tax(self, net_price, tax=23.0):
        tax_rate = tax / 100.0
        return net_price * tax_rate

    def capital_gains_tax(self, profit, tax=19.0):
        tax_rate = tax / 100.0
        if profit > 0:
            return profit * tax_rate
        return 0

import unittest
# from tax import SimpleTaxCalculator


def setUpModule():
    global calc
    calc = SimpleTaxCalculator()



class TestIncomeTax_4(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.calc = SimpleTaxCalculator()

    def test_income_below_threshold(self):
        self.assertEqual(calc.income_tax(60000), 10200)

    def test_income_equal_threshold(self):
        self.assertEqual(calc.income_tax(85528), 14539.76)

    def test_income_above_threshold(self):
        self.assertEqual(calc.income_tax(100000), 19170.8)


class TestVatTax_4(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.calc = SimpleTaxCalculator()

    def test_vat_tax_with_default(self):
        self.assertEqual(calc.vat_tax(100), 23.0)

    def test_vat_tax_with_twenty_tax_rate(self):
        self.assertEqual(calc.vat_tax(100, 20.0), 20.0)


class TestCapitalGainsTax_4(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.calc = SimpleTaxCalculator()

    def test_positive_profit(self):
        self.assertEqual(calc.capital_gains_tax(1000), 190.0)

    def test_zero_profit(self):
        self.assertEqual(calc.capital_gains_tax(0), 0.0)

    def test_negative_profit(self):
        self.assertEqual(calc.capital_gains_tax(-1000), 0.0)



#######################################################################################################
# EXERCISE 5
#######################################################################################################
'''
    The implementation of the Employee class is given in the emp.py file. In the solution 
    file (exercise.py) implement the TestEmployee class inheriting from unittest.TestCase. 
    Add one test method to this class:
        - test_email() which checks if the created employee (instance of the Employee class) with arguments:
            - 'John'
            - 'Smith'
            - 40
            - 80000
        has a valid email address: 'john.smith@mail.com'
'''
class Employee_5:
    """A simple class that describes an employee of the company."""

    tax_rate = 0.17

    def __init__(self, first_name, last_name, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary

    @property
    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@mail.com'

    @property
    def tax(self):
        return round(self.salary * self.tax_rate, 2)


# enter your solution here

class TestEmployee_5(unittest.TestCase):
    
    def test_email(self):
        actual = Employee_5(first_name='John', last_name='Smith', age=40, salary=80000)
        self.assertEqual('john.smith@mail.com', actual.email)




#######################################################################################################
# EXERCISE 6
#######################################################################################################
'''
    The implementation of the Employee class is given in the emp.py file. In the solution 
    file (exercise.py) add one test method to the TestEmployee class:

    - test_email_after_changing_first_name() which checks if the created employee 
    (instance of the Employee class) with arguments:

        - 'John'
        - 'Smith'
        - 40
        - 80000

    after changing the first name to 'Mike' has the correct email address: 'mike.smith@mail.com'
'''

class Employee_6:
    """A simple class that describes an employee of the company."""

    tax_rate = 0.17

    def __init__(self, first_name, last_name, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary

    @property
    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@mail.com'

    @property
    def tax(self):
        return round(self.salary * self.tax_rate, 2)

import unittest
# from emp import Employee


class TestEmployee_6(unittest.TestCase):

    def test_email(self):
        emp = Employee_6('John', 'Smith', 40, 80000)
        self.assertEqual(emp.email, 'john.smith@mail.com')
        
    # enter your solution here
    def test_email_after_changing_first_name(self):
        emp = Employee_6('John', 'Smith', 40, 80000)
        emp.first_name = 'Mike'
        self.assertEqual(emp.email, 'mike.smith@mail.com')


#######################################################################################################
# EXERCISE 7
#######################################################################################################
'''
    The implementation of the Employee class is given in the emp.py file. In the solution 
    file (exercise.py) add one test method to the TestEmployee class:
    - test_email_after_changing_last_name() which checks if the created employee 
    (instance of the Employee class) with arguments:
        - 'John'
        - 'Smith'
        - 40
        - 80000
    after changing the name to 'Doe' has the correct value of the email address: 'john.doe@mail.com'
'''

class Employee_7:
    """A simple class that describes an employee of the company."""

    tax_rate = 0.17

    def __init__(self, first_name, last_name, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary

    @property
    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@mail.com'

    @property
    def tax(self):
        return round(self.salary * self.tax_rate, 2)


import unittest
# from emp import Employee


class TestEmployee_7(unittest.TestCase):

    def test_email(self):
        emp = Employee_7('John', 'Smith', 40, 80000)
        self.assertEqual(emp.email, 'john.smith@mail.com')

    def test_email_after_changing_first_name(self):
        emp = Employee_7('John', 'Smith', 40, 80000)
        emp.first_name = 'Mike'
        self.assertEqual(emp.email, 'mike.smith@mail.com')

    # enter your solution here
    def test_email_after_changing_last_name(self):
        emp = Employee_7('John', 'Smith', 40, 80000)
        emp.last_name = 'Doe'
        self.assertEqual(emp.email, 'john.doe@mail.com')


#######################################################################################################
# EXERCISE 8
#######################################################################################################
'''
    The implementation of the Employee class is given in the emp.py file. In the solution 
    file (exercise.py) modify the TestEmployee class by adding the setUp() method that allows 
    for each test to recreate an instance of the Employee class with arguments: 'John', 
    'Smith', 40, 80000 and assign it to the TestEmployee class attribute named emp.
'''
class Employee_8:
    """A simple class that describes an employee of the company."""

    tax_rate = 0.17

    def __init__(self, first_name, last_name, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary

    @property
    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@mail.com'

    @property
    def tax(self):
        return round(self.salary * self.tax_rate, 2)

import unittest
# from emp import Employee


class TestEmployee_8(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        """ 
            Method that allows for each test to recreate an instance 
            of the Employee class with arguments
        """
        cls.emp = Employee_8('John', 'Smith', 40, 80000)

    def test_email(self):
        self.assertEqual(self.emp.email, 'john.smith@mail.com')

    def test_email_after_changing_first_name(self):
        self.emp.first_name = 'Mike'
        self.assertEqual(self.emp.email, 'mike.smith@mail.com')

    def test_email_after_changing_last_name(self):
        self.emp.last_name = 'Doe'
        self.assertEqual(self.emp.email, 'john.doe@mail.com')


#######################################################################################################
# EXERCISE 9
#######################################################################################################
'''
    The implementation of the Employee class is given in the emp.py file. The solution file 
    (exercise.py) contains the implementation of the TestEmployee class. Add two test methods 
    to this class:

    - test_get_salary() which checks if the value of the employee's salary 
    attribute is equal to 80000


    - test_apply_bonus() which checks whether the execution of the apply_bonus() method 
    of the Employee class correctly modifies the value of the salary attribute to 88000.
'''

class Employee_9:
    """A simple class that describes an employee of the company."""

    tax_rate = 0.17
    bonus_rate = 0.1

    def __init__(self, first_name, last_name, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary

    @property
    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@mail.com'

    @property
    def tax(self):
        return round(self.salary * self.tax_rate, 2)

    def apply_bonus(self):
        self.salary = int(self.salary * (1 + self.bonus_rate))

import unittest
# from emp import Employee


class TestEmployee_9(unittest.TestCase):

    def setUp(self):
        self.emp = Employee_9('John', 'Smith', 40, 80000)

    # enter your solution here
    def test_get_salary(self):
        actual = self.emp.salary
        self.assertEqual(actual, 80000)

    def test_apply_bonus(self):
        self.emp.apply_bonus()
        self.assertEqual(self.emp.salary, 88000)

#######################################################################################################
# EXERCISE 10
#######################################################################################################
'''
    The implementation of the Note class is given in notebook.py file. In exercise.py complete 
    the test_note_has_content_instance_attr() implementation to check if the Note instance has 
    an instance attribute called content. Also pass a message in case an assertion error is 
    raised, for example:
        'A Note instance does not have a content attribute.'
'''

import datetime


class Note:

    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now() \
            .strftime('%m-%d-%Y %H:%M:%S')

import unittest
# from notebook import Note


class TestNote_10(unittest.TestCase):

    def setUp(self):
        self.note = Note('Simple note.')
        
    def test_note_has_content_instance_attr(self):
        msg = 'A Note instance does not have a content attribute'
        self.assertTrue(hasattr(self.note, 'content'), msg)


#######################################################################################################
# EXERCISE 11
#######################################################################################################
'''
    The implementation of the Note class is given in notebook.py file. In exercise.py complete 
    the test_note_has_category_class_attr() implementation to check if the Note instance has an 
    instance attribute called category. Also pass a message in case an assertion error is raised, 
    for example:
        'The Note class does not have a category attribute.'
'''
import datetime


class Note_11:

    category = 'stock market'

    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')

import unittest
# from notebook import Note


class TestNote_11(unittest.TestCase):

    def test_note_has_category_class_attr(self):
        msg = 'The Note class does not have a category attribute.'
        self.assertTrue(hasattr(Note_11, 'category'), msg)


#######################################################################################################
# EXERCISE 12
#######################################################################################################
'''
    The implementation of the Note class is given in notebook.py file. In exercise.py complete 
    implementation of the test_notebook_search_method() to test the Notebook class's search() method. 
    Consider how to write the assertion correctly. Using the seach() method, check if the created notes 
    contain the word 'data' and compare with the expected result:
        ['Big Data', 'Data Science']
'''

import datetime


class Note_12:

    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime(
            '%m-%d-%Y %H:%M:%S')

    def find(self, word):
        return word.lower() in self.content.lower()


class Notebook_12:

    def __init__(self):
        self.notes = []

    def new_note(self, content):
        self.notes.append(Note_12(content))

    def search(self, value):
        return [note.content for note in self.notes if note.find(value)]


import unittest
# from notebook import Notebook


class TestNotebook_12(unittest.TestCase):

    def setUp(self):
        self.notebook = Notebook_12()
        self.notebook.new_note('Big Data')
        self.notebook.new_note('Data Science')
        self.notebook.new_note('Machine Learning')

    def test_notebook_search_method(self):
        actual = self.notebook.search('data')   # returns the notes in a dict if found
        expected = ['Big Data', 'Data Science']
        self.assertTrue(actual, expected)


#######################################################################################################
# EXERCISE 13
#######################################################################################################
'''
    The Employee class is implemented in employees.py file. In the exercise.py file complete the 
    test_employee_has_email_property(), which checks if the Employee class has an attribute named
    email as a property attribute. Do it in two steps:

    - Assert that the Employee class has an attribute named email - use the assertTrue() 
    assertion method and the hasattr() built-in function.

    - Assert whether the Employee class attribute named email is an instance of the built-in 
    property class or not - use the assertIsInstance() assertion method
'''

class Employee_13:
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

import unittest
# from employees import Employee


class TestEmployee_13(unittest.TestCase):

    def test_employee_has_email_property(self):
        self.assertTrue(hasattr(Employee_13, 'email'))
        self.assertIsInstance(Employee_13.email, property)


#######################################################################################################
# EXERCISE 14
#######################################################################################################
'''
    The implementation of the Product class in the products.py file is given. In exercise.py, 
    complete the test_product_has_get_id_function_attribute() implementation, which checks 
    if the Product class has a callable attribute called get_id.

    Do it in two steps:
        - Assert that the Product class has an attribute named get_id - use the assertTrue() 
        assertion method and the hasattr() built-in function.

        - Assert that the Product class attribute get_id is callable - use the assertTrue() 
        assertion method and the callable() built-in function.
'''

import uuid


class Product:

    def __init__(self, product_name, price):
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price

    def __repr__(self):
        return f"Product(product_name='{self.product_name}', price={self.price})"

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]

import unittest
# from products import Product


class TestProduct(unittest.TestCase):

    def test_product_has_get_id_function_attribute(self):
        self.assertTrue(hasattr(Product, 'get_id'))
        self.assertTrue(callable(Product.get_id))