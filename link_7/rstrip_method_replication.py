user_input = input("Type your full name: ")
last_non_space = len(user_input) - 1

while last_non_space >= 0 and user_input[last_non_space] == " ":
    last_non_space -= 1

print(user_input[:last_non_space + 1])