string = input("Enter a string: ")
sub = input("Enter substring to find: ")

for i in range(len(string) - len(sub) + 1):
    if all(string[i+j] == sub[j] for j in range(len(sub))):
        print(i)
        break
else:
    print(-1)