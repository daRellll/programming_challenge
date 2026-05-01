word = input("Enter a word: ")

if len(word) == 0:
    print("")
else:
    result = ""

    first = word[0]
    first_ascii = ord(first)
    if 97 <= first_ascii <= 122:
        result += chr(first_ascii - 32)
    else:
        result += first

    for i in range(1, len(word)):
        char = word[i]
        ascii_val = ord(char)
        if 65 <= ascii_val <= 90:
            result += chr(ascii_val + 32)
        else:
            result += char

    print(result)