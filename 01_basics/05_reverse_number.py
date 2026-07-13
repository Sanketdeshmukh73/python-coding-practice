# Question 5:
# Write a Python program to reverse a given number.

# Example 1:

# Input: 1234
# Output: 4321

# Example 2:

# Input: 9087
# Output: 7809

num = int(input("Enter the number: "))
reverse = 0

while num > 0:
    last_digit = num % 10
    reverse = reverse * 10 + last_digit
    num = num // 10
    
print(reverse)    
