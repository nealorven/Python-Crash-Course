# Page 220
# Тестирование класса. Разные методы assert

# Метод setUp() решает две задачи: он создает экземпляр опроса и список
# ответов. Каждый из этих атрибутов снабжается префиксом self, поэтому он
# может использоваться где угодно в классе.

import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Тесты для класса AnonymousSurvey."""

    def setUp(self):
        """Создание опроса и набора ответов для всех тестовых методов."""
        question = "What language did you first learn to speak?"

        self.responses = ['English', 'Spanish', 'Mandarin']
        self.my_survey = AnonymousSurvey(question)

    def test_store_single_response(self):
        """Проверяет, что один ответ сохранен правильно."""
        #     def store_response(self, new_response):
        #         self.responses.append(new_response)

        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Проверяет, что три ответа были сохранены правильно."""
        #     def store_response(self, new_response):
        #         self.responses.append(new_response)

        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()

# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
#
# OK
