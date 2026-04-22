user_input = input("Type something: ")
lowered_user_input = ""

for character in user_input:
    if 'A' <= character <= 'Z':
        lowered_user_input += chr(ord(character) + 32)
    else:
        lowered_user_input += character
print(lowered_user_input)