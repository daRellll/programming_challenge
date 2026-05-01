string = input("Enter a string: ")
suffix = input("Enter suffix to remove: ")

if len(suffix) > len(string):
    print(string)
else:
    start = len(string) - len(suffix)
    match = True

    for i in range(len(suffix)):
        if string[start + i] != suffix[i]:
            match = False
            break

    if match:
        print(string[:start])
    else:
        print(string)