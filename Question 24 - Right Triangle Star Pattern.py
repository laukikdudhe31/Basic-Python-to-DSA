# Problem:
# Print the following pattern:
# *
# **
# ***
# ****
# *****
# Rules:
# 1. Use only while loops.
# 2. Do NOT use a for loop.
# 3. Use two while loops (Nested Loop).
#Solution:-
i=1
while(i<=5):
    j=1
    while(j<=i):
        print("*",end="")
        j=j+1
    print()
    i=i+1