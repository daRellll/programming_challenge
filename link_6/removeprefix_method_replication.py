user_input = input("Type something: ")
prefix = input("Type the prefix you want to remove: ")

if user_input.startswith(prefix):
    print(user_input[len(prefix):])
else:
    print(user_input)