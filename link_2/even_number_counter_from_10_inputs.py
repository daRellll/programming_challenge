even_numbers_count = 0

for i in range(10):
    initial_input = float(input("input a number: "))
    
    if initial_input % 2 == 0:
        even_numbers_count += 1

print(even_numbers_count)