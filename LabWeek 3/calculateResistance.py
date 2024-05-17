# calculateResistance.py
# Author: Anish Reddy Nukala
# Date: 01-31-2024
# Lab Number: 3
# Description: Calculates voltage, current and prints resistance
# Citation: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwivhv2PtpmEAxXQIzQIHRVZDpEQFnoECBQQAw&url=https%3A%2F%2Fstudy.com%2Flearn%2Flesson%2Fresistance-equation-derivation.html%23%3A~%3Atext%3DHow%2520do%2520you%2520calculate%2520the%2Cthat%2520R%253DV%252FI.&usg=AOvVaw0qHMAjwMHnwoH4jOdo2Uvv&opi=89978449
import math

voltage= float(input("please enter the voltage value:"))
current= float(input("please enter the value of current:"))

resistance = voltage / current 

print(f"The resistance is {resistance} for current {current} and voltage {voltage}.")