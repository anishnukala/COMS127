# velocityAccelerationTime.py
# Author: Anish Reddy Nukala
# Date: 01-31-2024
# Lab Number: 3
# Description: Calculates speed and time and prints the distance
# Citation: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiMwZPotpmEAxWqLzQIHTSeD5AQFnoECBsQAQ&url=https%3A%2F%2Fwww.calculatorsoup.com%2Fcalculators%2Fphysics%2Fvelocity_a_t.php&usg=AOvVaw1KzxEcmUMah61gpuqPanEg&opi=89978449

import math

initial_Velocity= float(input("please enter initial velocity in meter per second:"))
acceleration= float(input("please enter acceleration in meters per second squared:"))
time = float(input("please enter time in seconds:"))

final_vcelocity = initial_Velocity + (acceleration * time)

print(f"The final velocity is {final_vcelocity} for initial velocity {initial_Velocity} in meter per second, acceleration {acceleration} in meters per second squared and time {time}.")