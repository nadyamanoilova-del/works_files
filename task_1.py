def count_lines_and_words():
    input_filename = 'input.txt'
    output_filename = 'statistics.txt'

    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        line_count = len(lines)

        word_count = 0
        for line in lines:
            words = line.strip().split()
            word_count += len(words)

        with open(output_filename, 'w', encoding='utf-8') as out_file:
            out_file.write(f"Задача 1: Счетчик строк и слов\n")
            out_file.write(f"Количество строк: {line_count}\n")
            out_file.write(f"Количество слов: {word_count}\n")

        print(f"Результаты успешно записаны в {output_filename}")

    except FileNotFoundError:
        print(f"Файл {input_filename} не найден.")


count_lines_and_words()