# Task 2
# Calculator
first_number = int(input("Enter First Number:"))
operator = (input("Enter Operator: "))
second_number = int(input("Enter Second Number:"))
if operator == "+":
    calculation = first_number + second_number
    print("Answer:", calculation)
if operator == "-":
    calculation = first_number - second_number
    print("Answer:", calculation)
if operator == "*":
    calculation = first_number * second_number
    print("Answer:", calculation)
if operator == "/" and second_number == 0:
    print("Scientific Error")
if operator == "/" and second_number != 0:
    calculation = first_number / second_number
    print("Answer:", calculation)


