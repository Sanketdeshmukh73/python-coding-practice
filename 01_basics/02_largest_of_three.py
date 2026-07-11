# Question 2:

# Write a Python program to take three numbers as input from the user
# and find the largest number among them.

# Example:
# Input:
# 10
# 25
# 15

# Output:
# Largest Number: 25


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"Largest Number: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"Largest Number: {num2}")
else:
    print(f"Largest Number: {num3}") 
