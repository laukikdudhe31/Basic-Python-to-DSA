# Problem:
# Take a number from the user.
# Print the sum of numbers from 1 to that number.
# Example 1:
# Input:
# 5
# Output:
# 15
# Explanation:
# 1 + 2 + 3 + 4 + 5 = 15

num=int(input("Enter your Number"))
i=1
total=0
while(i<=num):
    total=total+i
    i=i+1
print(total)