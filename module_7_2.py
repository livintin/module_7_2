def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    numbers_strings = 1
    for string in strings:
        numbers_byte = file.tell()
        file.write(f'{string}\n')
        strings_positions[(numbers_strings, numbers_byte)] = string
        numbers_strings += 1
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
