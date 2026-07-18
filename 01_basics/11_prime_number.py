# Problem Statement
# Write a Python program to check whether a given number is a Prime Number or not.

# Input
# Enter a number: 17

# Output
# 17 is a Prime Number



num = int(input("Enter the number: "))

if num <= 1:
    print(f"{num} is not a prime number")
else:
    i = 2
    while i * i <= num:
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
        i += 1
    else:
        print(f"{num} is a prime number")