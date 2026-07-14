# Question 9:
# Write a Python program to check whether a given
# number is an Armstrong Number or not.

# Example:
# Input: 153
# Output: Armstrong Number

# Explanation:
# 1³ + 5³ + 3³ = 153

num = int(input("Enter the number: "))
original = num
total = 0

while num > 0:
    digit = num % 10
    total += digit ** 3
    num = num // 10

if original == total:
    print("Armstrong number")
else:
    print("Not Armstrong number")    