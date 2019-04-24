import unittest

from population import get_format_city


class CountryTestCase(unittest.TestCase):
    def test_city_country(self):
        out_result = get_format_city('usa', 'new york')
        self.assertEqual(out_result, 'Usa, New York')

    def test_city_country_population(self):
        out_result = get_format_city('usa', 'new york', '130000')
        self.assertEqual(out_result, 'Usa, New York: 130000')


unittest.main()

# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK
