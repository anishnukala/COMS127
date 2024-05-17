
# sqrtlter.py
# Author: Anish Reddy Nukala
# Date: 02/07/2024
# Lab Number: 4
# Description: This program calculates the square root number of given number.
# Citation: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiN7q6BwpmEAxWCMjQIHZEjCZEQFnoECBUQAw&url=https%3A%2F%2Fbyjus.com%2Fsquare-root-calculator%2F%23%3A~%3Atext%3DThe%2520square%2520root%2520of%2520a%2Ca%2520root%2520symbol%2520or%2520surds.&usg=AOvVaw178HN-KA8tmKYnx4vlM8Fv&opi=89978449

import math

x=int(input('please enter a number:'))
iteration = int(input("please entre a number:"))

def sqrtIter(x, iteration):
    guess = (x+ 1/2 )
    for number in range(iteration):
        guess= (((x/guess) + guess)/2 )
    print(guess)

result= sqrtIter(x, iteration)
