# palindromeList.py
# Anish Reddy Nukala
# 02-28-2024
# Lab Number: 7
# Description: This program takes a list of strings from the user, determines whether all words are palindromic.

def take_input():
    palList = []
    while True:
        user_input = input("Enter a word (or * to exit): ")
        if user_input == "*":
            break
        palList.append(user_input)
    return palList
        

def palindromeList(palList):
            length = len(palList)
            for i in range(length // 2):
                if palList[i] != palList[length - i - 1]:
                    return False  
            return True 


def main():
    palListStr = take_input()
    print(palListStr)
    palOrNo = palindromeList(palListStr)
    print(f"It is " +  str(palOrNo) + " list is a palindrome")

if __name__ == "__main__":
    main()