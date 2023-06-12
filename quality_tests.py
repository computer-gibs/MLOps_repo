import app

def test_translation_quality():
    test_cases = [
        {
            "input": "Emma is writing a letter.",
            "expected_output": "Эмма пишет письмо.",
            "mode": "en-ru"
        },
        {
            "input": "Все счастливые семьи похожи друг на друга, каждая несчастливая семья несчастлива по-своему.",
            "expected_output": "All happy families are alike; every unhappy family is unhappy in its own way.",
            "mode": "ru-en"
        }
    ]

    for test_case in test_cases:
        input_text = test_case["input"]
        expected_output = test_case["expected_output"]
        mode = test_case["mode"]

        translated_text = app.translate(input_text, mode)
        assert translated_text.strip() == expected_output.strip(), f"Error in {mode} translation: Expected '{expected_output}', but got '{translated_text}'"

if __name__ == "__main__":
    test_translation_quality()
    print("All tests passed.")