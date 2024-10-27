import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    content = f.readlines()
                    words_list = []
                    for line in content:
                        line = line.lower()
                        line = line.translate(str.maketrans('', '', string.punctuation)).strip()
                        words = line.split()
                        words_list.extend(words)
                    all_words[file_name] = words_list
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        word = word.lower()
        for name, words in all_words.items():
            if word in words:
                result[name] = words.index(word) + 1
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        word = word.lower()
        for name, words in all_words.items():
            result[name] = words.count(word)
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))