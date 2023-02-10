
#######################################################################################################
# EXERCISE 1
#######################################################################################################
'''
    The CustomersDB class is implemented in the customers.py file. The TestCustomersDB class 
    is in the exercise.py file. Study carefully the implementation of both of these classes. 
    Then add a test method to the TestCustomersDB class named:

    test_add_customer(), which checks the add_customer() method of the CustomersDB class.

    Steps:

        In the test method create instance of the CustomersDB class:
            - db = CustomersDB(self.connection)

        Call the add_customer() method on the db instance adding the following client:
            - 'Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA'

        Create an instance of the Cursor class named cursor.

        Execute the following SQL code by calling the appropriate method of the Cursor class on the cursor instance:

            SELECT *
            FROM customers
            ORDER BY first_name, last_name;

        Assert the obtained result with the expected one.

    Expected result:
        expected = (
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        )
'''
class CustomersDB_1:

    def __init__(self, connection):
        self.connection = connection

    def add_customer(
        self,
        first_name,
        last_name,
        email,
        phone,
        country
    ):
        cursor = self.connection.cursor()
        sql = """
            INSERT INTO customers
            VALUES (:first_name, :last_name, :email, :phone, :country);"""
        cursor.execute(sql, locals())
        self.connection.commit()
        return cursor.lastrowid
    

import unittest
from sqlite3 import connect
# from customers import CustomersDB


class TestSFLDKSCustomersDB(unittest.TestCase):

    def setUp(self):
        connection = connect(':memory:')
        cursor = connection.cursor()

        create_table_sql = """
            CREATE TABLE customers 
            ( 
                first_name TEXT, 
                last_name  TEXT, 
                email      TEXT, 
                phone      TEXT, 
                country    TEXT 
            );"""
        cursor.execute(create_table_sql)

        customers_data = [
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA')
        ]

        insert_sql = """
            INSERT INTO customers
            VALUES (?, ?, ?, ?, ?);"""
        cursor.executemany(insert_sql, customers_data)

        self.connection = connection

    def tearDown(self):
        self.connection.close()

    # enter your solution here
    def test_add_customer(self):
        db = CustomersDB_1(self.connection)
        db.add_customer('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        cursor = self.connection.cursor()
        sql_query = "SELECT * FROM customers ORDER BY first_name, last_name;"
        expected = (
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        )
        actual = tuple(cursor.execute(sql_query))
        self.assertEqual(actual, expected)
    


#######################################################################################################
# EXERCISE 2
#######################################################################################################
'''
    The CustomersDB class is implemented in the customers.py file. The TestCustomersDB class is 
    in the exercise.py file. Study carefully the implementation of both of these classes. Then add a 
    test method to the TestCustomersDB class named:

    test_find_customers_by_first_name() which checks the find_customers_by_first_name() method of 
    the CustomersDB class.

    Steps:
        - In the test method create instance of the CustomersDB class:
        - db = CustomersDB(self.connection)

    Call find_customers_by_first_name() on the db instance.

    Assert the obtained result with the expected one.

    Expected result:

        expected = (
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA')
        )
'''
class CustomersDB_2:

    def __init__(self, connection):
        self.connection = connection

    def find_customers_by_first_name(self, first_name):
        cursor = self.connection.cursor()
        sql = """
            SELECT *
            FROM customers
            WHERE first_name LIKE :first_name
            ORDER BY first_name, last_name;"""
        cursor.execute(sql, locals())
        for row in cursor:
            yield row


import unittest
from sqlite3 import connect
# from customers import CustomersDB


class TestCustomersDB_2(unittest.TestCase):

    def setUp(self):
        connection = connect(':memory:')
        cursor = connection.cursor()

        create_table_sql = """
            CREATE TABLE customers 
            ( 
                first_name TEXT, 
                last_name  TEXT, 
                email      TEXT, 
                phone      TEXT, 
                country    TEXT 
            );"""
        cursor.execute(create_table_sql)

        customers_data = [
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        ]

        insert_sql = """
            INSERT INTO customers
            VALUES (?, ?, ?, ?, ?);"""
        cursor.executemany(insert_sql, customers_data)

        self.connection = connection

    def tearDown(self):
        self.connection.close()

    # enter your solution here
    def test_find_customers_by_first_name(self):
        db = CustomersDB_2(self.connection)
        actual = tuple(db.find_customers_by_first_name('John'))
        expected = (
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA')
        )
        self.assertEqual(actual, expected)



#######################################################################################################
# EXERCISE 3
#######################################################################################################
'''
    The CustomersDB class is implemented in the customers.py file. The TestCustomersDB class is 
    in the exercise.py file. Study carefully the implementation of both of these classes. Then 
    add a test method to the TestCustomersDB class named:

    test_find_customers_by_country() which checks the find_customers_by_country() method of 
    the CustomersDB class.

    Steps:
        - In the test method create instance of the CustomersDB class:

        - db = CustomersDB(self.connection)

        - Call the find_customers_by_country() method on the db instance.

        - Assert the obtained result with the expected one.

    Expected result:
        expected = (
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        )
'''
class CustomersDB_3:

    def __init__(self, connection):
        self.connection = connection

    def find_customers_by_country(self, country):
        cursor = self.connection.cursor()
        sql = """
            SELECT *
            FROM customers
            WHERE country LIKE :country
            ORDER BY first_name, last_name;"""
        cursor.execute(sql, locals())
        for row in cursor:
            yield row

import unittest
from sqlite3 import connect
# from customers import CustomersDB


class TestCustomersDB_3(unittest.TestCase):

    def setUp(self):
        connection = connect(':memory:')
        cursor = connection.cursor()

        create_table_sql = """
            CREATE TABLE customers 
            ( 
                first_name TEXT, 
                last_name  TEXT, 
                email      TEXT, 
                phone      TEXT, 
                country    TEXT 
            );"""
        cursor.execute(create_table_sql)

        customers_data = [
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('John', 'Doe', 'john.doe@mail.com', '333', 'Canada'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        ]

        insert_sql = """
            INSERT INTO customers
            VALUES (?, ?, ?, ?, ?);"""
        cursor.executemany(insert_sql, customers_data)

        self.connection = connection

    def tearDown(self):
        self.connection.close()

    # enter your solution here
    def test_find_customers_by_country(self):
        db = CustomersDB_3(self.connection)
        actual = tuple(db.find_customers_by_country('USA'))
        expected = (
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        )
        self.assertEqual(actual, expected)


