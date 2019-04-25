import unittest
from worker import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.first_name = 'neal'
        self.last_name = 'oaken'
        self.worker = Employee(self.first_name, self.last_name)

    def test_change_data_user(self):
        self.worker.change_data_user(self.first_name, self.last_name)
        self.assertIn(self.worker, self.worker)

    def test_set_annual_salary(self):
        pass

    def test_increase_annual_salary(self):
        pass

    def test_show_employee_value(self):
        self.worker.show_employee_value


    def test_city_country(self):
        out_result = get_format_city('usa', 'new york')
        self.assertEqual(out_result, 'Usa, New York')
