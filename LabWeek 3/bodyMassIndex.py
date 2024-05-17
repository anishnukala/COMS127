# bodyMassIndex.py
# Author: Anish Reddy Nukala
# Date: 01-31-2024
# Lab Number: 3
# Description: Calculates the body mass index by using our weight and height
#citation: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjqjq77tZmEAxV0CjQIHYHgD5EQFnoECBIQAw&url=https%3A%2F%2Fwww.cdc.gov%2Fhealthyweight%2Fassessing%2Fbmi%2Findex.html%23%3A~%3Atext%3DBody%2520Mass%2520Index%2520(BMI)%2520is%2Csquare%2520of%2520height%2520in%2520meters.&usg=AOvVaw26B2MGpfoaB8N0aNPddu6R&opi=89978449
import math

weight= float(input("please enter the weight:"))
height= float(input("please enter the height:"))

bmi = weight / (height ** 2) * 703

print(f"The Body mass Index is {bmi} for weight {weight} and height {height}.")