import unittest
from population import get_format_city


class CountryTestCase(unittest.TestCase):

    def test_city_country_population(self):
        # def get_format_city(city, country, population=''):
        #     if population:
        #         out_format = f"{city}, {country}: {population}"

        out_result = get_format_city('usa', 'new york', '130000')
        self.assertEqual(out_result, 'Usa, New York: 130000')

    def test_city_country(self):
        # def get_format_city(city, country, population=''):
        #     else:
        #         out_format = f"{city}, {country}"

        out_result = get_format_city('usa', 'new york')
        self.assertEqual(out_result, 'Usa, New York')


unittest.main()

# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK
