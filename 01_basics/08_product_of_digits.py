# Question 8:
# Write a Python program to find the product of all digits
# in a given number.

# Example:
# Input: 234
# Output: Product of Digits: 24

# Explanation:
# 2 * 3 * 4 = 24


num = int(input("Enter the number: "))
product = 1
while num > 0:
    last_digit = num % 10
    product = product * last_digit
    num = num // 10
print("Product of Digits:",product)    
