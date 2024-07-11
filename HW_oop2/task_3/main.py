def get_file_order(file_list):
    num_of_files = {}
    for file in file_list:
        with open(file, encoding='utf-8') as lines:
           num_of_files[file] = len(lines.readlines())

    sorted_files = sorted(num_of_files.items(), key=lambda item: item[1])
    return sorted_files


def create_new_file(file_order):
    with open('result.txt', 'w', encoding='utf-8') as new_file:
        for file in file_order:
            new_file.write(f'{file[0]}\n{file[1]}\n')
            with open(file[0], encoding='utf-8') as readed_file:
                for line in readed_file:
                    new_file.write(line)
            new_file.write('\n')


file_order = get_file_order(['1.txt', '2.txt', '3.txt'])
create_new_file(file_order)
