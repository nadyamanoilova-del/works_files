def combine_files():
    filenames = ['file1.txt', 'file2.txt', 'file3.txt']
    output_filename = 'combined.txt'
    separator = '\n' + '='*20 + '\n'

    try:
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            for filename in filenames:
                with open(filename, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content)
                    if filename != filenames[-1]:
                        outfile.write(separator)
        print(f"Файлы успешно объединены в {output_filename}")
    except FileNotFoundError as e:
        print(f"Ошибка: {e}. Проверьте наличие файлов {', '.join(filenames)}.")

combine_files()