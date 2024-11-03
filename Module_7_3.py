# Задача "Найдёт везде":

# # Test file
# test_txt = [
#     "It's a text for task Найти везде,",
#     "Используйте его для самопроверки.",
#     "Успехов в решении задачи!",
#     "text text text"
# ]
#
# with open("test_file.txt", "w", encoding='utf-8') as file:
#     for line in range(len(test_txt)):
#         file.write(test_txt[line] + "\n")
#
# with open('test_file.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line.strip())

def big_print():
    for i in range(3):
        print()


class WordsFinder:
    # Вноси любое количество txt файлов
    def __init__(self, *file_name):
        self.file_name = file_name

    def get_all_words(self):
        # Пустой словарь
        all_words = {}
        # знаки пунктуации
        punction = [',', '.', '=', '!', '?', ';', ':']
        # вынес отдельно для упрощения
        one_punct = " - "

        # перебор по-файлово
        for file_name in self.file_name:
            # открываем, читаем
            with open(file_name, 'r', encoding='utf-8') as file:
                # создаем пустой словарь для слов каждому перебираемому файлу свой
                words = []
                # по строке в файле
                for line in file:
                    # приводим строки к нижнему регистру
                    line = line.lower()
                    # по символьнов в списке пунктуации
                    for punct in punction:
                        line = line.replace(punct, '')
                    # И отдельно для тире
                    line = line.replace(one_punct, '')
                    # добавляем в конец списка итерируемые объекты
                    # любого типа благодаря .extend()
                    words.extend(line.split())
                # в словарь по ключу - название файла, по значению - полученный список слов к нему
                all_words[file_name] = words
        return all_words


    def find(self, word):
        position = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                position[key] = value.index(word.lower()) + 1

        return position




    def count(self, word):
        counters = {}
        for value, key in self.get_all_words().items():
            words_counter = key.count(word.lower())
            counters[value] = words_counter

        return counters


# ДЗ
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

big_print()

# Доп ДЗ
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

big_print()

#