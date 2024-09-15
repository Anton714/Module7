def custom_write(file_name: str, strings: list = []):
    file = open(file_name, 'a')
    file.close()
    strings_positions: dict = {}
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(len(strings)):
        poz = file.tell()
        file.write(f'{strings[i]}\n')
        strings_positions.setdefault((i + 1, poz), strings[i])

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
