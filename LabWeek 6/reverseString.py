#reverseString.py
#Anish Reddy Nukala
#02-28-2024
#Lab 6
# Description: From user input it will find the reverse string values 


def reverseStringV1(input_string):
    # Reverse the string using string slicing
    reversed_string = input_string[::-1]
    return reversed_string

def reverseStringV2(input_string):
    # Reverse the string without using string slicing
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

def main():
    # Take input from the user
    input_string = input("Enter a string: ")

    # Version 1: Reverse the string using slicing
    reversed_string_v1 = reverseStringV1(input_string)
    print(f"Version 1: {input_string} => {reversed_string_v1}")

    # Version 2: Reverse the string without slicing
    reversed_string_v2 = reverseStringV2(input_string)
    print(f"Version 2: {input_string} => {reversed_string_v2}")

if __name__ == "__main__":
    main()