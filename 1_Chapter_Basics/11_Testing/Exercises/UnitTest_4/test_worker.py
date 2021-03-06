import unittest
from workers import give_raise


class TestEmployee(unittest.TestCase):

    def test_give_custom_raise(self):
        """Повышение на конкретную сумму"""
        #     def give_raise(self, up_raise=''):
        #         if up_raise:
        #             self.annual_salary += up_raise

        #first_name, last_name, annual_salary = 'neal', 'oaken', 3000
        # worker = Employee(first_name, last_name, annual_salary)
        # worker.give_raise()

        out_result = give_raise(3000)
        self.assertEqual(out_result, 'Annual salary: 3000$')

    #def test_give_default_raise(self):
        #"""Повышение по умолчанию"""
        # #     def give_raise(self, up_raise=''):
        #         else:
        #             self.annual_salary += 5000
        #pass


unittest.main()
