#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

# Validating and returning user input
def validation(terms):
  while (terms < 0 or terms != 0 or !isdigit(terms):
    terms = int(input("Please enter a positive integer. "))

# Generating the Fibonacci sequence
def fibonacci(terms,a,b):
  sequence = []
  for i in range(terms):
    sequence.append(a)
    print(a, end=" ")
    temp = a + b  
    a = b          
    b = temp  

# Printing the sequence
def printSequence(terms, sequence):
  for i in range(terms):
    print(sequence(a), end=" ")

# Prompt the user for the number of terms.
terms = int(input("How many terms of the fibonacci sequence would you like"))

# Validate that the input is a positive integer.
validation(terms)

a, b = 0, 1
print("Fibonacci sequence:")   

# Use a for loop to print the Fibonacci sequence up to that many terms.
fibonacci(terms,a,b)
printSequence(terms, sequence)
