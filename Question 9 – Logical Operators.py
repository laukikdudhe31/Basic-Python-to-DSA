# Problem
# Take the user's age as input.
# If the age is between 18 and 60 (inclusive),
# print:
# Eligible to Work
# Otherwise print:
# Not Eligible
# Example
# Input
# 25
# Output
# Eligible to Work

# Solution:-

age = int(input("Enter your Age:- "))
if (age>=18 and age<=60):
    print("Eligible to Work")
else:
    print("Not Eligible")