string = input("Enter a string: ")
prefix = input("Enter prefix to check: ")

if len(prefix) > len(string):
    print(False)
else:
    match = True

    for i in range(len(prefix)):
        if string[i] != prefix[i]:
            match = False
            break

    print(match)