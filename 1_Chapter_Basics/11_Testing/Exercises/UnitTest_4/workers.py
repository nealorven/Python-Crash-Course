class Employee:

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, up_raise=''):
        if up_raise:
            self.annual_salary = up_raise
        else:
            self.annual_salary += 5000

    def read_raise(self):
        print(f"Annual salary: {self.annual_salary}.")


worker = Employee('neal', 'oaken', '3000')
worker.read_raise()
# Annual salary: 3000.

worker.give_raise()
