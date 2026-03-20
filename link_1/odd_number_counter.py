number_list = []

for i in range(10):
    number = float(input("Enter a number: "))
    if number % 2 != 0:
        number_list.append(number)

print("The odd number count is:", len(number_list))