user_input = input("Type your full name: ")

i = len(user_input)
while i > 0 and user_input[i-1] == " ":
    i -= 1

print(user_input[:i])