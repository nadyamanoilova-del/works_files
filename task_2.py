def search_word_in_file():
    search_word = input("Введите слово для поиска: ").strip()
    filename = 'text.txt'
    found = False
    count = 0
    lines_with_word = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file, start=1):
                if search_word in line:
                    found = True
                    count += line.count(search_word)
                    lines_with_word.append(i)

        if found:
            print(f"Слово '{search_word}' найдено.")
            print(f"Количество встреч: {count}")
            print(f"Строки, в которых встречается: {', '.join(map(str, lines_with_word))}")
        else:
            print(f"Слово '{search_word}' не найдено.")

        with open('search_results.txt', 'w', encoding='utf-8') as result_file:
            if found:
                result_file.write(f"Слово '{search_word}' найдено.\n")
                result_file.write(f"Количество встреч: {count}\n")
                result_file.write(f"Строки: {', '.join(map(str, lines_with_word))}\n")
            else:
                result_file.write(f"Слово '{search_word}' не найдено.\n")
        print("Результаты записаны в search_results.txt")
    except FileNotFoundError:
        print("Файл text.txt не найден.")

search_word_in_file()