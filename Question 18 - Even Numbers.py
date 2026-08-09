#Problem:
# Take a number from the user.
# Print all even numbers from 1 to that number.
# Example:
# Input:
# 10
# Output:
# 2
# 4
# 6
# 8
# 10

number=int(input("Enter your no:- "))
i=1
while(i<=number):
    if(i%2==0):
        print(i)
    i=i+1