string = input("Enter a string: ")
suffix = input("Enter suffix to remove: ")

start = len(string) - len(suffix)
match = start >= 0 and all(string[start + i] == suffix[i] for i in range(len(suffix)))

print(string[:start] if match else string)