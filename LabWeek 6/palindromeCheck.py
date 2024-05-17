#palindromeCheck.py
#Anish Reddy Nukala
#02-28-2024
#Lab 6
# Description: This palindrome will help user to know whether it is palindrome or not

from reverseString import reverseStringV1

def palindromeCheckV1(input_string):
    reversed_string = reverseStringV1(input_string)

    if reversed_string == input_string:
        return True
    else:
        return False

def palindromeCheckV2(input_string):
    left, right = 0, len(input_string) - 1

    while left < right:
        if input_string[left] != input_string[right]:
            return False
        left += 1
        right -= 1

    return True

def main():
    input_string = input("Enter a string: ")

    is_palindrome_v1 = palindromeCheckV1(input_string)
    if is_palindrome_v1:
        print(f"Version 1: '{input_string}' is a palindrome.")
    else:
        print(f"Version 1: '{input_string}' is not a palindrome.")

    is_palindrome_v2 = palindromeCheckV2(input_string)
    if is_palindrome_v2:
        print(f"Version 2: '{input_string}' is a palindrome.")
    else:
        print(f"Version 2: '{input_string}' is not a palindrome.")

if __name__ == "__main__":
    main()
