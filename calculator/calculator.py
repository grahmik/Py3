#!/bin/python3
# Mike G 4/29/2023

####    Welcome to the calculator!      ####
####    I was given the challenge       #### 
####   by my mentor to use functions    ####
####  that are imported from separate   ####
####  py scripts. This was a quick way  ####
####   to show that I understand that   ####
####         concept. Enjoy!            ####


# Imports
from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide
import time


while True:
    print("\nSelect operation:\n")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    operation = float(input("\nChoose 1, 2, 3, or 4: "))
    
    if operation not in (1, 2, 3, 4):
        print("\033[91mPlease pick a valid option\033[0m")
        time.sleep(1)
        continue

    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == 1:
        print(num1, "+", num2, "=", add(num1, num2))
    elif operation == 2:
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif operation == 3:
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif operation == 4:
        print(num1, "/", num2, "=", divide(num1, num2))

    repeat = input("\nWould you like to do another calculation? (Yes or No): ").lower()

    if repeat == "yes":
        continue
    else:
        print("Goodbye!")
        break
