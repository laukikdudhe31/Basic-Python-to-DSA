# Problem:
# Print the following pattern:
# 12345
# 1234
# 123
# 12
# 1
# Rules:
# 1. Use only while loops.
# 2. Do NOT use a for loop.
# 3. Use two while loops (Nested Loop).
#Solution:-
i=5
while(i>=1):
    j=1
    while(j<=i):
        print(j,end="")
        j=j+1
    print()
    i=i-1
