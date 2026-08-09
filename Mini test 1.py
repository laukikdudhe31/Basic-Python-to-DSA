# Write a Python program that:
# Takes the user's age as input.
# Takes whether the user has an ID card as input (yes or no).
# If the user's age is 18 or above and the user has an ID card (yes), print:
# Allowed
# Otherwise print:
# Not Allowed
# Rules
# Use int(input()) for age.
# Use input() for the ID card.
# Use the and operator.
# Use if-else.

age=int(input("Enter your age"))
Id=input("If you have ID card so please enter as(yes or no).")

if(age>=18 and Id=="yes"):
    print("Allowed")
else:
    print("Not Allowed")
    