def caesar_encrypt(text, shift=3):
    result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def caesar_decrypt(text, shift=3):
    return caesar_encrypt(text, -shift)

def encrypt_file():
    try:
        with open('secret.txt', 'r', encoding='utf-8') as infile:
            plaintext = infile.read()
        encrypted_text = caesar_encrypt(plaintext)
        with open('encrypted.txt', 'w', encoding='utf-8') as outfile:
            outfile.write(encrypted_text)
        print("Текст успешно зашифрован и сохранен в encrypted.txt")
    except FileNotFoundError:
        print("Файл secret.txt не найден.")

def decrypt_file():
    try:
        with open('encrypted.txt', 'r', encoding='utf-8') as infile:
            encrypted_text = infile.read()
        decrypted_text = caesar_decrypt(encrypted_text)
        with open('decrypted.txt', 'w', encoding='utf-8') as outfile:
            outfile.write(decrypted_text)
        print("Текст успешно расшифрован и сохранен в decrypted.txt")
    except FileNotFoundError:
        print("Файл encrypted.txt не найден.")

encrypt_file()
decrypt_file()