# bookAnalysis.py
# Anish Reddy Nukala
# Date: 03-27-2024
# Lab Week 11

import string

def analyze_book(file_name):
    try:
        with open(file_name, 'r') as f:
            count = {}
            for line in f:
                words = line.split()
                for word in words:
                    word = word.strip(string.punctuation).lower()
                    if word.isalpha():
                        count[word] = count.get(word, 0) + 1
            return count
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return None

def output_analysis(counts, title):
    try:
        with open(f'{title}_analysis.txt', 'w') as out:
            sorted_words = sorted(counts.keys())
            for word in sorted_words:
                out.write(f"{word} {counts[word]}\n")
            print("Analysis saved successfully.")
            return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    file_name = input("Enter the name of the book file: ")
    title = file_name.split('.')[0]
   
    count_dict = analyze_book(file_name)
   
    if count_dict is not None:
        succeeded = output_analysis(count_dict, title)
        print("Did the output succeed?", succeeded)

if __name__ == "__main__":
    main()