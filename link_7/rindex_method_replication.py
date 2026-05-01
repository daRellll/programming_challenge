string = input("Enter a string: ")
sub = input("Enter substring to find: ")

found = -1

for start in range(len(string) - len(sub) + 1):
    match = True

    for i in range(len(sub)):
        if string[start + i] != sub[i]:
            match = False
            break

    if match:
        found = start

print(found)