word = input("Enter a word: ")

if len(word) == 0:
    print("")
else:
    result = word[0].upper() + word[1:].lower()
    print(result)