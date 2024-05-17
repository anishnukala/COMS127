# catAttack.py
# Anish Reddy Nukala
# Date: 02-04-2024
# Lab Week 12 

def catStrike(x):
    print("Meow " + str(x) + "!")

def catAttack(cat):
    for i in range(0, len(cat)):
        catStrike(cat[i])

def main():
    catAttack("TOM")

if __name__ == "__main__":
    main()