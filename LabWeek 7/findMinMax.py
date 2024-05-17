# findMinMax.py
# Anish Reddy Nukala
# 02-28-2024
# Lab Number: 7
# Description: This program takes a list of string representations of integers from the user

def takeInput():
    numbers = []
    while True:
        user_input = input("Enter a number (or * to finish): ")
        if user_input == '*':
            break
        else:
            numbers.append(user_input)
    return numbers

def convertToIntegers(numbers):
    return [int(num) for num in numbers]

def findMin(numbers):
    if not numbers:
        return None
    min_value = int(numbers[0])
    for num in numbers:
        if int(num) < min_value:
            min_value = int(num)
    return min_value

def findMax(numbers):
    if not numbers:
        return None

    max_value = int(numbers[0])
    for num in numbers:
        if int(num) > max_value:
            max_value = int(num)
    return max_value

def main():
    numbers = takeInput()
    integers = convertToIntegers(numbers)

    min_value = findMin(integers)
    max_value = findMax(integers)

    print(f"The minimum value is: {min_value}")
    print(f"The maximum value is: {max_value}")

if __name__ == "__main__":
    main()
