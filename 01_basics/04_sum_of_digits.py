# Question 4:
# Write a Python program to take a number as input from the user
# and find the sum of all digits in the number.

# Example:
# Input: 1234
# Output: Sum of Digits: 10

# Explanation:
# 1 + 2 + 3 + 4 = 10


num = int(input("Enter the number: "))
total = 0
while num > 0:
    last_digit = num % 10
    total += last_digit
    num = num // 10
print(total)    




