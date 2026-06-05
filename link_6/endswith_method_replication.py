string = input("Enter a string: ")
suffix = input("Enter the suffix to check: ")

if len(suffix) == 0:
    print(True)
else:
    match = len(suffix) <= len(string) and string[-len(suffix):] == suffix
    print(match)