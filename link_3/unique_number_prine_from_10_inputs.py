numbers = set()
duplicate_numbers = set()

for i in range(10):
    user_input = float(input("Enter a mumber: "))
    
    if user_input in numbers:
        duplicate_numbers.add(user_input)
    else:
        numbers.add(user_input)
        
print(numbers - duplicate_numbers)