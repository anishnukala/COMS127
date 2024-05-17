#wordswap.py
# Anish Reddy Nukala
# Date: 03-27-2024
# Lab Week 11
import random

def swap_words(sentence):
    words = sentence.split()
    unique_words = list(set(words))
    random.shuffle(unique_words)
    word_dict = {word: new_word for word, new_word in zip(words, unique_words)}

    print("Original sentence words and their swaps:")
    print(word_dict)

    new_sentence = " ".join(word_dict[word] for word in words)
    print("New sentence:")
    print(new_sentence)

def main():
    user_input = input("Enter a complete sentence: ")
    swap_words(user_input)

if __name__ == "__main__":
    main()