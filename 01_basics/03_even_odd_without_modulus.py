# Question 3:
# Write a Python program to check whether a given number is Even or Odd
# WITHOUT using the modulus (%) operator.

# Example:
# Input: 8
# Output: Even Number

# Input: 7
# Output: Odd Number


num = int(input("Enter the number: "))
if num//2 == num/2:
    print("Even Number")
else:
    print("Odd Number")    