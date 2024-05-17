# countGoalRecursive.py
# Anish Reddy Nukala
# Date: 02-04-2024
# Lab Week 12 

def countDownGoalRecursive(n, goal):
    if n >= goal:
        print(n)
        countDownGoalRecursive(n - 1, goal)


def countUpGoalRecursive(n, goal):
    if n >= goal:
        countUpGoalRecursive(n - 1, goal)
        print(n)

def main():

    n = 5
    goal = 3
    countDownGoalRecursive(n, goal)
    countUpGoalRecursive(n, goal)


if __name__ == "__main__":
    main()

