# palindromeList.py
# Anish Reddy Nukala
# 02-28-2024
# Lab Number: 7
# Description: This program takes a list of strings from the user, determines whether all words are palindromic.


def take_input():
    palindrome_list = []
    while True:
        user_input = input("Enter a string (or * to finish): ")
        if user_input == '*':
            break
        else:
            palindrome_list.append(user_input)
    return palindrome_list

def is_palindrome(word):
    return word == word[::-1]

def is_palindrome_list(palindrome_list):
    return all(is_palindrome(word) for word in palindrome_list)

def main():
    palindrome_list = take_input()
    
    if is_palindrome_list(palindrome_list):
        print("The list is palindromic!")
    else:
        print("The list is not palindromic.")

if __name__ == "__main__":
    main()
