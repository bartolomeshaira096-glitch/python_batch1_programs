def prog01():
 num1 = float(input("Enter first number: "))
 num2 = float(input("Enter second number: "))
if num1 > num2:
        print(num1)
else:
        print(num2)
def prog02():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num1 == num2:
        print("Equal")
def prog03():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    total_sum = num1 + num2
    print(total_sum)
def prog04():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    product = num1 * num2
    print(product)
def prog05():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Cannot divide by zero")
def prog06():
    base_number = float(input("Enter first number: "))
    exponent_number = float(input("Enter second number: "))
    print(base_number ** exponent_number)
def prog07():
    total_sum = 0
    for i in range(10):
        number = float(input(f"Enter number {i+1}: "))
        total_sum += number
    print("Total sum:", total_sum)
def prog08():
    odd_count = 0
    for i in range(10):
        number = int(input(f"Enter number {i+1}: "))
        if number % 2 != 0:
            odd_count += 1
    print("Odd numbers count:", odd_count)
def prog09():
    for number in range(0, 101):
        if number % 2 == 0:
            print(number)
def prog10():
    # FOR number from 0 to 100
    # IF number mod 10 != 0
    #     DISPLAY number
