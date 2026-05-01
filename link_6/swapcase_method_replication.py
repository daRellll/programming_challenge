word = input("Enter a word: ")
result = ""

for char in word:
    ascii_char = ord(char)

    if 65 <= ascii_char <= 90:
        result += chr(ascii_char + 32)
    elif 97 <= ascii_char <= 122:
        result += chr(ascii_char - 32)
    else:
        result += char

print(result)