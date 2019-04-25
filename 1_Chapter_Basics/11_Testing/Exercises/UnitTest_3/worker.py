class Employee:

    def __init__(self, first_name, last_name, annual_salary=''):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = int(annual_salary)

    def change_data_user(self, first_name, last_name):
        """Изменить учетные данные"""
        self.first_name = first_name
        self.last_name = last_name

    def set_annual_salary(self, set_salary):
        """Установить годовой оклад"""
        self.annual_salary = int(set_salary)

    def increase_annual_salary(self, incr_salary):
        """Увеличить годовой оклад"""
        self.annual_salary += incr_salary

    def show_employee_value(self):
        """Вывод информации о пользователе"""
        f_name = f"First name: {self.first_name}."
        l_name = f"Last name: {self.last_name}."
        a_salary = f"Annual salary: {self.annual_salary}."
        return f_name.title(), l_name.title(), a_salary


worker = Employee('neal', 'oaken', '5000')
worker.show_employee_value()
# First name: Neal.
# Last name: Oaken.
# Annual salary: 5000.

worker.set_annual_salary(7000)
worker.show_employee_value()
# First name: Neal.
# Last name: Oaken.
# Annual salary: 7000.
