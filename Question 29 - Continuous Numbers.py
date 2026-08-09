# Problem:
# Print the following pattern:
# 12345
# 678910
# 1112131415
# 1617181920
# 2122232425
# Rules:
# 1. Use only while loops.
# 2. Do NOT use a for loop.
# 3. Use two while loops (Nested Loop).
# 4. Use an extra variable to keep track of the number.

num = 1

i = 1
while(i <= 5):
    j = 1
    while(j <= 5):
        print(num, end="")
        num=num+1
        j = j + 1
    print()
    i = i + 1