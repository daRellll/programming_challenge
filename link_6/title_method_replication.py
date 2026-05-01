word = input("Enter a word: ")
result = ""
new_word = True

for char in word:
    ascii_val = ord(char)
    is_upper = 65 <= ascii_val <= 90
    is_lower = 97 <= ascii_val <= 122
    is_letter = is_upper or is_lower

    if new_word and is_letter:
        result += chr(ascii_val - 32) if is_lower else char
        new_word = False
    elif is_letter:
        result += chr(ascii_val + 32) if is_upper else char
    else:
        result += char
        if char == " ":
            new_word = True

print(result)