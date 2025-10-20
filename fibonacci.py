#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def fibonacci(terms,a,b):
  for i in range(terms):
    print(a, end=" ")
    temp = a + b  
    a = b          
    b = temp  

# Prompt the user for the number of terms.
terms = int(input("How many terms of the fibonacci sequence would you like"))
# Validate that the input is a positive integer.
while (terms < 0 or terms != 0 or !isdigit(terms):
  terms = int(input("Please enter a positive integer. "))
a, b = 0, 1
print("Fibonacci sequence:")    
# Use a for loop to print the Fibonacci sequence up to that many terms.
fibonacci(terms,a,b)
