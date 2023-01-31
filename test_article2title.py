import unittest # pragma: no cover
from article2title import * # pragma: no cover

class Test_article2title(unittest.TestCase): # pragma: no cover
    def test_article2title_001(self):
        # проверим на статью меньше 25 символов
        article = "test 1 2 3"
        actual = article2title(article)
        expected = article

        self.assertEqual(actual, expected)
        self.assertLessEqual(len(actual), 25) # проверка, что заголовок меньше или равен 25 

    def test_article2title_002(self):
        # проверем на статью больше 25 символов
        article = "Volvo released a new car with the following spec: V6 236HP. It will cost $22647"
        actual = article2title(article)
        expected = "Volvo released a new..."

        self.assertEqual(actual, expected)
        self.assertLessEqual(len(actual), 25) # проверка, что заголовок меньше или равен 25
        if len(article) > 25: # проверка, что если статья больше 25 символов, то заголовок заканчивается на "..."
            self.assertEqual(actual[-3:], "...")

    def test_article2title_003(self):
        # проверем на слово больше 25 символов
        article = "hippopotomomonstrosesquippedaliophobia"
        actual = article2title(article)
        expected = ""

        self.assertEqual(actual, expected)
        self.assertLessEqual(len(actual), 25) # проверка, что заголовок меньше или равен 25 

    def test_article2title_004(self):
        # если часть статьи со вторым слово в сумме больше 25 символом то вернем первое слово с тремя точками
        article = "Hi! hippopotomomonstrosesquippedaliophobia"
        actual = article2title(article)
        expected = "Hi!..."

        self.assertEqual(actual, expected)
        self.assertLessEqual(len(actual), 25) # проверка, что заголовок меньше или равен 25
        if len(article) > 25: # проверка, что если статья больше 25 символов, то заголовок заканчивается на "..."
            self.assertEqual(actual[-3:], "...")

    def test_article2title_005(self):
        # если статья пустая вернем пустую
        article = ""
        actual = article2title(article)
        expected = article

        self.assertEqual(actual, expected)
        self.assertLessEqual(len(actual), 25) # проверка, что заголовок меньше или равен 25 

    def test_article2title_006(self):
        # если статья ровно 25 символов - вернем статью
        article = "авто квазигосударственный"
        self.assertEqual(len(article), 25) # проверка, что статья равна 25

        actual = article2title(article)
        expected = article

        self.assertEqual(actual, expected)
        self.assertLessEqual(len(actual), 25) # проверка, что заголовок меньше или равен 25
