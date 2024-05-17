# statisticsList.py
# Anish Reddy Nukala
# 02-28-2024
# Lab Number 7
# Description: This program generates a random list of integers, calculates the mean and median,and prints the results.

import random

def generateInput():
    length = random.randint(200, 500)
    random_list = [random.randint(1, 2000) for _ in range(length)]
    return random_list

def findMean(random_list):
    
    total = 0
    for num in random_list:
        total += num
    mean = total / len(random_list)
    return mean

def findMedian(random_list):
    
    sorted_list = sorted(random_list)
    length = len(sorted_list)
    
    if length % 2 == 1:
        median = sorted_list[length // 2]
    else:
        middle1 = sorted_list[length // 2 - 1]
        middle2 = sorted_list[length // 2]
        median = (middle1 + middle2) / 2
    
    return median

def main():
    random_list = generateInput()
    
    mean = findMean(random_list)
    median = findMedian(random_list)

    print("Mean: {0} Median: {1}".format(mean, median))

if __name__ == "__main__":
    main()
