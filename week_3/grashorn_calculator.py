#
#     Title: grashorn_calculator.py
#     Author: Brett Grashorn
#     Date: 27 March 2023
#     Description: File for Assignment 3.3. Creating a calculator
#     using Python.
#     Sources: WEB-335
#     W3 Schools
#

# Add function with two parameters
def add(x, y):
    return x + y

# Subtract function with two parameters


def subtract(x, y):
    return x - y

# divide function with two parameters


def divide(x, y):
    return x / y

# multiply function with two parameters


def multiply(x, y):
    return x * y


# Tests the add function

# Initializes the variables
num1 = 4
num2 = 4
# Stores the result of the function
sum_of_twonumbers = add(num1, num2)

print("{0} + {1} is {2}."
      .format(num1, num2, sum_of_twonumbers))  # Returns 4 + 4 is 8.

# Tests the Subtract function

# Initializes the variables
num1 = 10
num2 = 6

# Stores the result of the function
difference_of_twonumbers = subtract(num1, num2)

print("{0} - {1} is {2}."
      .format(num1, num2, difference_of_twonumbers))  # Returns 10 - 6 is 4.

# Tests the divide function

# Initializes the variables
num1 = 8
num2 = 2

# Stores the result of the function
quotient_of_twonumbers = divide(num1, num2)

print("{0} / {1} is {2}."
      .format(num1, num2,
              quotient_of_twonumbers))  # Returns 8 / 2 is 4.0.

# Tests the multiply function

# Initializes the variables
num1 = 10
num2 = 2

# Stores the result of the function
product_of_twonumbers = multiply(num1, num2)

print("{0} * {1} is {2}." .format(num1, num2, product_of_twonumbers)  # Returns 10 * 2 is 20.
      )
