# ЗАПИСАТЬ И ЗАПОМНИТЬ

import io

def custom_write(file_name, strings):
    strings_positions = {}
    coords = ()

    ##########   Запись в файл
    create_file = open(file_name, 'w')
    write_symb_start_line = 0
    write_line = 1
    j = 0
    for string in strings:
#       print(write_line, write_symb_start_line)
#       print("Symbol with tell(): ", create_file.tell())
        coords += write_line, create_file.tell()
        write_line += 1
        write_symb_start_line += len(string) + 1
        create_file.write(string + '\n')
    create_file.close()
    #
    # print()
    # print(coords)
    #
    # print()

    #######   Чтение из файла
    read_file = open(file_name, 'r')
    lines = 1
    symbols = 0
    j = 0
    for line in read_file:

        new_coords = coords[j], coords[j+1]
        strings_positions[new_coords] = line.strip()
        #print(((coords[j], coords[j + 1]), '' + line.strip() + ''))

        j += 2
        lines += 1
        symbols += len(line)

    read_file.close()
    return strings_positions



# # Пример выполняемого кода:
# #
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
#
result = custom_write('test.txt', info)
# print(result)

for elem in result.items():
    print(elem)
