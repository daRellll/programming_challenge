string = input("Enter a string: ")
sub = input("Enter substring to find: ")

found = -1
for i in range(len(string) - len(sub) + 1):
    if string[i:i+len(sub)] == sub:
        found = i

print(found)