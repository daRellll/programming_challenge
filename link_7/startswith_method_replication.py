string = input("Enter a string: ")
prefix = input("Enter prefix to check: ")

print(len(prefix) <= len(string) and all(string[i] == prefix[i] for i in range(len(prefix))))