# Problem:
# Print the following pattern:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# Rules:
# 1. Use only while loops.
# 2. Do NOT use a for loop.
# 3. Use a third variable to keep track of the numbers.

num=1

i=1
while(i<=5):
    j=1
    while(j<=i):
        print(num,end=" ")
        num=num+1
        j=j+1
    print()
    i=i+1