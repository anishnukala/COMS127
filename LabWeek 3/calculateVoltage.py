# calculateVoltage.py
# Author: Anish Reddy Nukala
# Date: 01-31-2024
# Lab Number: 3
# Description: Calculates current and resistance and prints the voltage
# Citation: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjGjfSbtpmEAxU1JDQIHWJWDI8QFnoECE8QAQ&url=https%3A%2F%2Fwww.fluke.com%2Fen-us%2Flearn%2Fblog%2Felectrical%2Fwhat-is-ohms-law&usg=AOvVaw1nyNfDK73D-MLpGaSLAHxa&opi=89978449
import math

current= float(input("please enter the value of current:"))
resistance= float(input("please enter the value of resistance:"))

voltage = current * resistance

print(f"The voltage is {voltage} for current {current} and resistance {resistance}.")