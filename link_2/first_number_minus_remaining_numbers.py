number_list = []
first_number = float(input("Enter your first number: "))
for i in range(9):
    number_list.append(float(input("Enter a number: ")))

print(first_number - sum(number_list))