# Problem:
# Take a number from the user.
# Print numbers from that number down to 1.
# Example:
# Input:
# 5
# Output:
# 5
# 4
# 3
# 2
# 1

num=int(input("Enter your num"))
i=num
while(i>=1):
    print(i)
    i=i-1