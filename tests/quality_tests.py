import os
import subprocess
from app import translate
translate.path.append("..")


def test_translation_quality(input_text, expected_output, mode):
    result = translate(input_text, mode=mode)
    assert result == expected_output, f"Expected '{expected_output}', but got '{result}'"


def run_quality_tests():
    test_translation_quality("Emma is writing a letter.",
                             "Эмма пишет письмо.",
                             mode="en-ru")

    test_translation_quality(
        "Все счастливые семьи похожи друг на друга, каждая несчастливая семья несчастлива по-своему.",
        "All happy families are alike; every unhappy family is unhappy in its own way.",
        mode="ru-en")

    print("All quality tests passed.")


if __name__ == "__main__":
    run_quality_tests()