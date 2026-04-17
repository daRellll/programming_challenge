numbers = []
most_duplicate_number = None

while True:
    try:
        user_input = float(input("Enter a number: "))
        
        numbers.append(user_input)
        
        if most_duplicate_number is None:
           most_duplicate_number = user_input
        elif numbers.count(user_input) < numbers.count(most_duplicate_number):
            pass
        else:
            most_duplicate_number = user_input
                              
            
    except ValueError: 
             break 

print(most_duplicate_number)