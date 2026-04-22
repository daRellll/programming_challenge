user_input = input("Type your full name: ")
number_of_space = 0

while number_of_space < len(user_input) and user_input[number_of_space] == " ":
    number_of_space += 1

print(user_input[number_of_space:])