# Question 6:
# Write a Python program to check whether a given number
# is a Palindrome Number or not.

# Example 1:
# Input: 121
# Output: Palindrome Number

# Example 2:
# Input: 123
# Output: Not a Palindrome Number


num = int(input("Enter the number: "))
original = num   #121
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")

