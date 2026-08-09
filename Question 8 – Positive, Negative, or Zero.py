# Problem
# Take one integer as input.
# Print:
# "Positive" if the number is greater than 0.
# "Negative" if the number is less than 0.
# "Zero" if the number is equal to 0.
# Example
# Input
# -5
# Output
# Negative
num=int(input("Enter your number:-"))
if(num>0):
    print("Positive")
elif (num==0):
    print("Zero")
else:
    print("Negative")