def custom_write(file_name, strings):
    strings_positions = {}

    # Открываем файл для записи в режиме 'w' (перезапись)
    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings):
            # Получаем текущую позицию в байтах перед записью
            byte_position = file.tell()
            # Записываем строку в файл с переходом на новую строку
            file.write(string + '\n')
            # Сохраняем в словарь номер строки и позицию в байтах
            strings_positions[(index + 1, byte_position)] = string

    return strings_positions

# Пример выполняемого кода
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

# Вывод результата
for elem in result.items():
    print(elem)
