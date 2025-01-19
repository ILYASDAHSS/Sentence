class String:
    def __init__(self, string):
        self.string = string

    def display(self):
        print(self.string)


class Sentence(String):
    def __init__(self, string, language):
        super().__init__(string)
        self.language = language

    def display(self):
        print(f"Sentence in {self.language}: {self.string}")

    def get_type(self):
        last_character = self.string[-1] 
        if last_character == '?':
            return "interrogative"
        elif last_character == '!':
            return "exclamatory"
        else:
            return "declarative"

    def longest_word(self):
        words = self.string.split()
        longest_word = max(words, key=len)
        return f"{longest_word} ({len(longest_word)} characters)"


if __name__ == "__main__":
    sentence1 = Sentence("Hello world", "English")
    sentence1.display()
    print("Type of sentence:", sentence1.get_type())
    print("Longest word:", sentence1.longest_word())