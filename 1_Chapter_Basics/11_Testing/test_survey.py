import unittest
from survey import AnonymousSurvey


class TestAnonmyousSurvey(unittest.TestCase):
    """Тесты для класса AnonymousSurvey"""

    def test_store_single_response(self):
        """Проверяет, что один ответ сохранен правильно."""
        question = "What language did you first learn to speak?"
        # Новый экземпляр
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """Проверяет, что три ответа были сохранены правильно."""
        question = "What language did you first learn to speak?"
        # Новый экземпляр
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)


unittest.main()

# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s
#
# OK
#
# C:\Repository\Python-Crash-Course\1_Chapter_Basics\11_Testing>test_survey.py
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
#
# OK
