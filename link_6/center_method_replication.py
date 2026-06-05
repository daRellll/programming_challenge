word = input("Enter a word: ")
char_fill = input("Enter a char: ")
total_width = int(input("Enter how much to add: "))

padding = max(0, total_width - len(word))
print(char_fill * (padding // 2) + word + char_fill * (padding - padding // 2))