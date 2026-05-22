duplicate_numbers = set()

while True:
    try:
        user_input = float(input("Enter a number: "))
        if user_input in duplicate_numbers:
            print("Duplicate")       
        else:
            print("Unique")
        duplicate_numbers.add(user_input)
    except ValueError: 
             break 
