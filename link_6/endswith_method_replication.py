string = input("Enter a string: ")
suffix = input("Enter the suffix to check: ")

if len(suffix) == 0:
    print(True)
elif len(suffix) > len(string):
    print(False)
else:
    match = True
    string_index = len(string) - len(suffix)

    for i in range(len(suffix)):
        if string[string_index + i] != suffix[i]:
            match = False
            break

    print(match)