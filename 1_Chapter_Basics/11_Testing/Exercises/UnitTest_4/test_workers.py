import unittest
from workers import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.first_name = 'neal'
        self.last_name = 'oaken'
        self.annual_salary = 0

        self.worker = Employee(
            self.first_name,
            self.last_name,
            self.annual_salary)

    def test_give_default_raise(self):
        pass

    def test_give_custom_raise(self):
        pass
