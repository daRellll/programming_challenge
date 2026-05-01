word = input("Enter a word: ")
length_of_padding = int(input("Enter the amount of padding you want to add: "))
left_padding = max(0, length_of_padding - len(word))

print(word + " " * left_padding)