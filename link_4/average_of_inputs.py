numbers = []

while True:
    try:
        user_input = float(input("Enter a number: "))

        numbers.append(user_input)

    except ValueError: 
             break 

average = sum(numbers) / len(numbers)

print(average)