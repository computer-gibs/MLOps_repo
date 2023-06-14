import unittest
from app import translate

class TestApp(unittest.TestCase):

    def test_en_ru_translation(self):
        input_text = "My name is Sarah, I live in London"
        expected_output = "Меня зовут Сара, я живу в Лондоне"
        result = translate(input_text, mode="en-ru")
        self.assertEqual(expected_output, result)

        input_text = ""
        expected_output = ""
        result = translate(input_text, mode="en-ru")
        self.assertEqual(expected_output, result)

    def test_ru_en_translation(self):
        input_text = "Привет, как дела?"
        expected_output = "Hello, how are you doing?"
        result = translate(input_text, mode="ru-en")
        self.assertEqual(expected_output, result)

        input_text = ""
        expected_output = ""
        result = translate(input_text, mode="ru-en")
        self.assertEqual(expected_output, result)

if __name__ == "__main__":
    unittest.main()