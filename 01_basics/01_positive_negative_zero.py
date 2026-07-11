# Question 1:
# Write a Python program to take a number as input from the user
# and check whether the number is Positive, Negative, or Zero.



# Example:
# Input: 10
# Output: Positive Number

# Input: -5
# Output: Negative Number

# Input: 0
# Output: Zero
#--------------------------------------------------------------------------------------

num = int(input("Enter The Number: "))
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")