# Question 7:
# Write a Python program to count the total number of digits
# in a given number.

# Example 1:
# Input: 12345
# Output: Total Digits: 5

# Example 2:
# Input: 789
# Output: Total Digits: 3


num = int(input("Enter the number: "))
count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        count = count + 1
        num = num // 10

print("Total Digits:", count)        
