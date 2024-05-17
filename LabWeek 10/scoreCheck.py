# scoreCheck.py
# Anish Reddy Nukala
# Date: 03-20-2024
# Lab Week 10 

def main():
    threshold = int(input("What is the threshold value?: "))

    with open("studentData.txt", "r") as file:
        for line in file:
            words = line.split()
            name = words[0]
            scores = [int(score) for score in words[1:]]
            greater_than_threshold = sum(score >= threshold for score in scores)
            less_than_threshold = sum(score < threshold for score in scores)
            print(f"{name}: {greater_than_threshold} scores >= {threshold}, {less_than_threshold} scores < {threshold}")

if __name__ == "__main__":
    main()
