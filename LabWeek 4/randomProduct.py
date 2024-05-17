# randomProduct.py
# Author: Anish Reddy Nukala
# Date: 02/07/2024
# Lab Number: 4
# Description: This program takes input from the user and shows us random numbers

import random
def randomProduct(a, b, c):
    product = 1
    for _ in range(a):
        product *= random.randrange(b, c + 1)
    return product

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

result = randomProduct(a, b, c)

print(f"The product of {a} random numbers between {b} and {c} is: {result}")