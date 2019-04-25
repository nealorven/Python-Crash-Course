import unittest
from workers import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.first_name = 'neal'
        self.last_name = 'oaken'
        self.annual_salary = 0

        self.worker = Employee(
            self.first_name, self.last_name, self.annual_salary)

    def test_give_custom_raise(self):
        """Повышение на конкретную сумму"""
        #     def give_raise(self, up_raise=''):
        #         if up_raise:
        #             self.annual_salary += up_raise

        self.worker.give_raise(self.annual_salary)
        self.assertIn(self.annual_salary, self.worker.annual_salary)

    def test_give_default_raise(self):
        """Повышение по умолчанию"""
        # #     def give_raise(self, up_raise=''):
        #         else:
        #             self.annual_salary += 5000

        pass
