#Problem:
# Take a number from the user.
# Print its multiplication table from 1 to 10.
# Example:
# Input:
# 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50

#solution:-

num=int(input("Enter your number:- "))
i=num
j=1
while(j<=10):
    print(f"{i}x{j}={i*j}")
    j=j+1