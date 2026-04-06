lowest_number = None

while True:
    try:
        user_input = float(input("Enter a number: "))
        
        if lowest_number is None:
            lowest_number = user_input
        elif lowest_number < user_input:
            pass
        else:
            lowest_number = user_input
            
    except ValueError: 
             break 

print(lowest_number)