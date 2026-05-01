string = input("Enter a string: ")
width = int(input("Enter total width: "))

padding = max(0, width - len(string))
print(" " * padding + string)