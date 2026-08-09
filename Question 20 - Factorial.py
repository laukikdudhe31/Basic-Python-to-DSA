# Problem:
# Take a number from the user.
# Print the factorial of that number.
# Example:
# Input:
# 5
# Output:
# 120
# Explanation:
# 5! = 5 × 4 × 3 × 2 × 1 = 120

num=int(input("Enter your number:- "))
i=1
total=1
while(i<=num):
    total=total*i
    i=i+1
print(total)