string = input("Enter a string: ")
has_lower = False
has_upper = False

for char in string:
    if 'a' <= char <= 'z':
        has_lower = True
    elif 'A' <= char <= 'Z':
        has_upper = True

print(has_lower and not has_upper)