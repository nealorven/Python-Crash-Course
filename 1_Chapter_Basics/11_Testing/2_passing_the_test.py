# Page 211
# Прохождение теста

import unittest
from name_function import get_formatted_name
#from name_function_middle import get_formatted_name
#from name_function_middle_2 import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Тесты для 'name_function.py'."""

    # Любой метод который начинается с test_, будет выполняться автоматически.
    def test_first_last_name(self):
        """Имена вида 'Janis Joplin' работают правильно?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


unittest.main()
