"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:The user enters the integer N
# 2. Process: The program checks numbers from 1 to N to see if it is odd or even
# 3. Out: A list of numbers showing whether the numbers are odd or even
# 4. What happens on 0, on a negative number, on a very large number:
#0 : Displays a message since it's neither odd or even
# Negative number: Error message 
# 5000: Displays a message asking the user to enter a smaller number 


# Your code below
N = int(input("Enter a number:"))
if N == 0:
    print("There are no numbers to check.")

elif N < 0:
    print("Please enter a positive number.")

elif N > 100: 
    print("The number is too large. Please enter a number up to 100.")

else:
    for number in range(1, N + 1):
        if number % 2 == 0:
            print(number, "it's even")
        else:
            print(number, "is odd")

# Test N = 6: 3 odd and 3 even numbers, as expected.
# Test N = 0: A message is displayed because there are no numbers to check.
# Test N = -4: A message asks for a positive number.
# Test N = 5000: A message asks for a number up to 100.
