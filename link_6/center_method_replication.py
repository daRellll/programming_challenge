word = input("Enter a word: ")
char_fill = input("Enter a char: ")
total_width = int(input("Enter how much to add: "))

padding_needed = max(0, total_width - len(word))
left_padding = padding_needed // 2
right_padding = padding_needed - left_padding

print(char_fill * left_padding + word + char_fill * right_padding)