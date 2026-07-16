# Question 10:
# Write a Python program to check whether a given number
# is a Strong Number or not.

# Example:
# Input: 145
# Output: Strong Number

# Explanation:
# 1! + 4! + 5! = 145
#--------------------------------------------------------------------------------

num = int(input("Enter the number: "))
total = 0
original = num

while num > 0:
    digit = num % 10

    factorial = 1
    i = 1

    while i <= digit:
        factorial = factorial * i
        i = i + 1


    total = total + factorial
    num = num // 10


if original == total:
    print("Strog Number")
else:
    print("Not Stong Number")    

    
