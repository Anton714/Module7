class WordsFinder:

    def __init__(self, *file_name):
        self.file_names = file_name

    def __str__(self, str):

        str_l = str.lower()
        str_l = str_l.replace(',', '')
        str_l = str_l.replace('.', '')
        str_l = str_l.replace('=', '')
        str_l = str_l.replace('!', '')
        str_l = str_l.replace('?', '')
        str_l = str_l.replace(';', '')
        str_l = str_l.replace(':', '')
        str_l = str_l.replace('-', '')
        
        return str_l

    def get_all_words(self):

        all_words: dict = {}
        for _name in self.file_names:
            with open(_name, encoding='utf-8') as file:
                list_ = []
                for str in file:
                    list_.extend(self.__str__(str).split())
                all_words.setdefault(_name, list_)

        return all_words

    def find(self, word):
        dict_w = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                dict_w.setdefault(name, words.index(word.lower()) + 1)
        return dict_w

    def count(self, word):
        dict_count = {}
        for name, words in self.get_all_words().items():
            word_count = words.count(word.lower())
            dict_count.setdefault(name, word_count)

        return dict_count


finder1 = WordsFinder('Rudyard Kipling - If.txt')
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
