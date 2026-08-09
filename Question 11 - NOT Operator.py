# Problem
# Take the user's answer as input.
# The user will enter either:
# yes
# no
# If the answer is not "yes", print:
# Access Denied
# Otherwise print:
# Access Granted
#Solution:-

Input=input("Enter your answer")
if not Input == "yes":
    print("Access Denied")
else:
    print("Access Granted")