# Anish Reddy Nukala            02-12-2024
# Assignment 2 
# This Calculator helps user to calculate operators like (+,-,*) and lucky Number

import random

print("Lucky Calculator!")
print()

print("By: Anish Reddy Nukala")
print("[COM S 127 B]")
print()

def getInput():
    input_1 = int(input("Enter the first integer: "))
    input_2 = int(input("Enter the second integer: "))
    
    return input_1, input_2

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero. Setting divisor to 1.")
        b = 1
    return a / b

def floor_divide(a, b):
    if b == 0:
        print("Error: Cannot perform floor division by zero. Setting divisor to 1.")
        b = 1
    return a // b

def modulus(a, b):
    if b == 0:
        print("Error: Cannot perform modulus by zero. Setting divisor to 1.")
        b = 1
    return a % b

def exponentiate(a, b):
    return a ** b

def luckyNumber(a, b):
    return random.randint(a, b)

print("Welcome to the lucky Calculator!")

while True:
    print("Choose an option: ")
    print("[c]alculator, [l]ucky number, or [q]uit")
    
    choice = input("Enter your choice: ")
    
    if choice == 'c':
        operation = input("Enter the operation (+, -, *, /, //, %, **): ")
        num1, num2 = getInput()

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        elif operation == '//':
            result = floor_divide(num1, num2)
        elif operation == '%':
            result = modulus(num1, num2)
        elif operation == '**':
            result = exponentiate(num1, num2)
        else:
            print("Invalid operation. Please try again.")
            continue

        print(f"Result: {result}")

    elif choice == 'l':
        num1, num2 = getInput()
        lucky_num = luckyNumber(num1, num2)
        print(f"Your lucky number is: {lucky_num}")

    elif choice == 'q':
        print("Goodbye! Thank you was using it.")
        break

    else:
        print("Invalid choice. Please enter 'c', 'l', or 'q'.")