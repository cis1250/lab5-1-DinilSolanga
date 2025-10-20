#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

# Validating and returning user input
def validation(terms):
  while terms <= 0:
        try:
            terms = int(input("Please enter a positive integer: "))
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
            terms = 0  # force loop again
    return terms

# Generating the Fibonacci sequence
def fibonacci(terms):
  a, b = 0, 1
  sequence = []
  for i in range(terms):
    sequence.append(a)
    print(a, end=" ")
    a, b = b, a + b
  return sequence

# Printing the sequence
def printSequence(terms, sequence):
  for i in sequence:
    print(i, end=" ")

# Prompt the user for the number of terms.
try:
    terms = int(input("How many terms of the Fibonacci sequence would you like? "))
except ValueError:
    terms = 0

# Validate that the input is a positive integer.
validation(terms)


print("Fibonacci sequence:")   

# Use a for loop to print the Fibonacci sequence up to that many terms.
sequence = fibonacci(terms)
printSequence(terms, sequence)
