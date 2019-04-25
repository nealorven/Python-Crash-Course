# Page 216
# Тестирование класса. Разные методы assert

# Класс unittest.TestCase содержит целое семейство проверочных методов assert.

# Методы assert, предоставляемые модулем unittest
# Метод                         Использование
# assertEqual(a, b)             Проверяет, что a == b
# assertNotEqual(a, b)          Проверяет, что a != b
# assertTrue(x)                 Проверяет, что значение x истинно
# assertFalse(x)                Проверяет, что значение x ложно
# assertIn(элемент, список)     Проверяет, что элемент входит в список
# assertNotIn(элемент, список)  Проверяет, что элемент не входит в список


class AnonymousSurvey:
    """Сбор анонимных ответов на опросы."""

    def __init__(self, question):
        """Сохраняет вопрос и готовится к сохранению ответов."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Выводит вопрос."""
        print(self.question)

    def store_response(self, new_response):
        """Сохраняет один ответ на опрос."""
        self.responses.append(new_response)

    def show_results(self):
        """Выводит все полученные ответы."""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)
