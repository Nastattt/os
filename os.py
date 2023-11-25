import os
# def read_end(lines, file):
#     if not isinstance(lines, int) or lines <= 0:
#         raise ValueError("Число должно быть целым")
#
#     try:
#         with open(file, 'r', encoding='utf-8') as f:
#             content = f.readlines()
#
#
#             for line in content[-lines:]:
#                 print(line.strip())
#     except FileNotFoundError:
#         print(f"'{file}' не существует")
#
#
# # Пример использования
# read_end(5, 'article.txt')
#
#
#
#
#
#
# def print_reps(directory):
#     for root, dirs, files in os.walk(directory):
#         print(f"Подкаталоги в {root}: {dirs}")
#         print(f"Файлы в {root}: {files}")
#         print()
#
# print_reps('./venv')

#
# def longest_words(file_path):
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             content = file.read()
#
#             # Разделяем текст на слова
#             words = content.split()
#
#             # Находим максимальную длину слова(ов)
#             max_length = max(len(word) for word in words)
#
#             # Выбираем слова с максимальной длиной
#             longest_words_list = [word for word in words if len(word) == max_length]
#
#             return longest_words_list
#
#     except FileNotFoundError:
#         return "Файл не найден."
#
#
# # Пример использования
# file_path = 'poem.txt'
# result = longest_words(file_path)
#
# if isinstance(result, list):
#     print(f"Самые длинные слова в файле {file_path}: {', '.join(result)}")
# else:
#     print(result)
#



def text_statistics(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            # Первый проход для подсчета букв латинского алфавита
            latin_letters_count = sum(1 for char in content if char.isalpha() and char.isascii())

            # Второй проход для подсчета слов и строк
            words_count = len(content.split())
            lines_count = content.count('\n') + 1

            return {
                'Количество букв латинского алфавита': latin_letters_count,
                'Число слов': words_count,
                'Число строк': lines_count
            }

    except FileNotFoundError:
        return "Файл не найден."

# Пример использования
file_path = 'file.txt'
result = text_statistics(file_path)

if isinstance(result, dict):
    for key, value in result.items():
        print(f'{key}: {value}')
else:
    print(result)



