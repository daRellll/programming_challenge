user_input = input("Type something: ")
has_upper = False
has_lower = False

for character in user_input:
    if 'A' <= character <= 'Z':
        has_upper = True
    elif 'a' <= character <= 'z':
        has_lower = True

is_uppercase = has_upper and not has_lower

print(is_uppercase)