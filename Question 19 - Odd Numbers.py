# Problem:
# Take a number from the user.
# Print all odd numbers from 1 to that number.
# Example:
# Input:
# 10
# Output:
# 1
# 3
# 5
# 7
# 9
#Solution:-

num=int(input("Enter the number :- "))
i=1
while(i<=num):
    if(not i%2==0):
        print(i)
    i=i+1