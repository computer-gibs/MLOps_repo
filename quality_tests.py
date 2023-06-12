import sys
import app
import unittest

class TestTranslationModel(unittest.TestCase):

    def test_en_ru_translation(self):
        input_text = "Emma is writing a letter."
        expected_output = "Эмма пишет письмо."
        translated_text = app.translate(input_text, mode="en-ru")
        self.assertEqual(translated_text.strip(), expected_output)

    def test_ru_en_translation(self):
        input_text = "Все счастливые семьи похожи друг на друга, каждая несчастливая семья несчастлива по-своему."
        expected_output = "All happy families are alike; every unhappy family is unhappy in its own way."
        translated_text = app.translate(input_text, mode="ru-en")
        self.assertEqual(translated_text.strip(), expected_output)

    def test_empty_input(self):
        input_text = ""
        expected_output = ""
        translated_text_en_ru = app.translate(input_text, mode="en-ru")
        translated_text_ru_en = app.translate(input_text, mode="ru-en")
        self.assertEqual(translated_text_en_ru.strip(), expected_output)
        self.assertEqual(translated_text_ru_en.strip(), expected_output)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)