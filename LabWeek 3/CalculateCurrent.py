# calculateCurrent.py
# Author: Anish Reddy Nukala
# Date: 01-31-2024
# Lab Number: 3
# Description: Calculates voltage, current and prints resistance
# Citation: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiq-P6HtpmEAxWSJzQIHX9mAI0QFnoECBEQAw&url=https%3A%2F%2Fstudy.com%2Facademy%2Flesson%2Fflow-of-electric-charge-equation-application.html%23%3A~%3Atext%3DElectric%2520current%2520can%2520be%2520calculated%2C%2522R%2522%2520stands%2520for%2520resistance.&usg=AOvVaw2Vz62s-A91ax3JSSjgPlhX&opi=89978449

import math

voltage= float(input("please enter the voltage value:"))
resistance= float(input("please enter the value of resistance:"))

current = voltage / resistance

print(f"The value of current  is {current} for resistance {resistance} and voltage {voltage}.")