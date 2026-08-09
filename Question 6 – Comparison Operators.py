# Problem

# Take two numbers as input from the user.

# Print the result of the following comparisons:

# Is the first number greater than the second?
# Is the first number less than the second?
# Are both numbers equal?
# Example

# Input

# 10
# 20

# Output

# Greater: False
# Less: True
# Equal: False

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))

greater = num1 > num2
less = num1 < num2
equal = num1 == num2

print("Greater:", greater)
print("Less:", less)
print("Equal:", equal)