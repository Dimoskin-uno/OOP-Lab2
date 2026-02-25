class TextProcessor:
    def process(self, text):
        if not isinstance(text, str):
            raise TypeError("Вхідні дані повинні бути текстовим рядком")

        sentences = text.split(".")
        clean_sentences = []
        for sentence in sentences:
            sentence = sentence.strip()
            if sentence:
                clean_sentences.append(sentence)

        if not clean_sentences:
            raise ValueError("Текст не містить жодного коректного речення")

        sorted_sentences = sorted(
            clean_sentences,
            key=lambda s: len(s.split()))

        string_builder = []
        for i, sentence in enumerate(sorted_sentences):
            string_builder.append(sentence)
            if i < len(sorted_sentences) - 1:
                string_builder.append(". ")
            else:
                string_builder.append(".")

      result = "".join(string_builder)
        return result
if __name__ == "__main__":
    text = (
        "Football is the most popular sport. "
        "Ukraine is the largest country in Europe. "
        "Python became the programming language of 2024."
    )
    processor = TextProcessor()
    result = processor.process(text)
    print("Речення у порядку зростання кількості слів:")
    print(result)
