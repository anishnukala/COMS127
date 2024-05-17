# distanceSpeedTime.py
# Author: Anish Reddy Nukala
# Date: 01-31-2024
# Lab Number: 3
# Description: Calculates speed and time and prints the distance
# Citation: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj31YPMtpmEAxWYAzQIHVNNB48QFnoECBEQAw&url=https%3A%2F%2Fwww.bbc.co.uk%2Fbitesize%2Farticles%2Fzhbtng8%23%3A~%3Atext%3DThe%2520formula%2520can%2520be%2520rearranged%2Ctime%2520%253D%2520distance%2520%25C3%25B7%2520speed&usg=AOvVaw2igXr6WkDcnUTdOWhSercE&opi=89978449

import math

speed= float(input("please enter speed in meter per second:"))
time= float(input("please enter time in second:"))

distance = speed * time

print(f"The distance is {distance} for speed {speed} in meter per second and time {time}.")