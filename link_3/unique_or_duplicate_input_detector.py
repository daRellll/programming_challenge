numbers = set()
duplicate_numbers = set()

while True:
    try:
        user_input = float(input("Enter a number: "))
        
        if user_input in numbers:
            duplicate_numbers.add(user_input) 
            print("Duplicate")       
        else:
            numbers.add(user_input)
            print("Unique")
    except ValueError: 
             break 
