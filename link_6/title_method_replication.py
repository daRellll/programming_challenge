word = input("Enter a word: ")
result = ""
new_word = True

for char in word:
    if char == " ":
        result += char
        new_word = True
    elif new_word:
        result += char.upper()
        new_word = False
    else:
        result += char.lower()

print(result)