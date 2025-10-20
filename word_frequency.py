#!/usr/bin/env python3

import re
import string

# Append words function

def frequency(words, frequencies):
    for word in words_list:
    if word in words:
        index = words.index(word)
        frequencies[index] += 1
    else:
        words.append(word)
        frequencies.append(1)


# This function is provided — do not modify
def is_sentence(text):
    if not isinstance(text, str) or not text.strip():
        return False
    if not text[0].isupper():
        return False
    if not re.search(r'[.!?]$', text):
        return False
    if not re.search(r'\w+', text):
        return False
    return True


user_sentence = input("Enter a sentence: ")

while not is_sentence(user_sentence):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")

sentence = user_sentence.lower()

for p in string.punctuation:
    sentence = sentence.replace(p, "")

words_list = sentence.split()

words = []
frequencies = []
frequency(words, frequencies)
for i in range(len(words)):
    print(f"{words[i]}: {frequencies[i]}")
