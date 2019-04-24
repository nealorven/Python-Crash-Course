import unittest

from city_and_country import get_format_city


class CountryTestCase(unittest.TestCase):
    def test_city_country(self):
        out_result = get_format_city('usa', 'new york')
        self.assertEqual(out_result, 'Usa, New York')


unittest.main()

# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK
