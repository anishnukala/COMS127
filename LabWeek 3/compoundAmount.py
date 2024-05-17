# compoundAmount.py
# Author: Anish Reddy Nukala
# Date: 01-31-2024
# Lab Number: 3
# Description: Calculates compund intrest
# Citation: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwijrrK9tpmEAxU6IjQIHUO-B5AQFnoECDcQAQ&url=https%3A%2F%2Fwww.calculatorsoup.com%2Fcalculators%2Ffinancial%2Fcompound-interest-calculator.php&usg=AOvVaw0kLTfrHkDyD_YYh_ASwZ9j&opi=89978449

import math

principle= float(input("please enter the principle amount:"))
rate= float(input("please enter the rate of intrest:"))
number_Compounds= float(input("please enter the intrest compounds in a year:"))
time= float(input("please enter the time period:"))

accured_amount= principle * ( 1 + (rate/100) / number_Compounds) ** (number_Compounds * time)

print(f"The accured amount is {accured_amount}.")