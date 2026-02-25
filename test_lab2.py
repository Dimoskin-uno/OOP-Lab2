import unittest
from text_processor import TextProcessor
class TestTextProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = TextProcessor()

    def test_correct_sorting(self):
        text = (
            "Football is the most popular sport. "
            "Ukraine is the largest country in Europe. "
            "Python became the programming language of 2024."
        )
        result = self.processor.process(text)

        expected = (
            "Football is the most popular sport. "
            "Ukraine is the largest country in Europe. "
            "Python became the programming language of 2024."
        )
        self.assertEqual(result, expected)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            self.processor.process(123)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            self.processor.process("   .   .")
if __name__ == "__main__":
    unittest.main()
