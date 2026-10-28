"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:The user enters yes or no to approve a marketing campaign. 
# 2. Process:The program keeps asking until the campaign is approved or the max number of attempts is reached. 
# 3. Out:A summary showing if the campaign was approved and number of attempts.
# 4. My stop condition, my attempt limit, my summary:
# My stop condition is when the user answers "yes".
# Maximum attempts: 5.
# The summary shows the approval status and number of attempts.
# Capital letters and extra spaces are accepted.

# Your code below
attempts = 0
max_attempts = 5
approved = False

while attempts < max_attempts and not approved:
    answer = input("Do you approve the marketing campaign? (yes/no):")
    attempts += 1
    if answer.strip().lower()== "yes":
        approved = True
        print("Campaign approved")

    else:
        print("Campaign not approved")

#Summary:
print("Total attempts:", attempts)
if approved:
    print("Final: Approved")
else:
    print("Final: Not approved")

# Test 1: Entered "no" five times. The program stopped after 5 attempts.
# Test 2: Entered " YES " with capitals and spaces. The program accepted it.
# Test 3: Entered "no", "no", "yes". The program stopped after 3 attempts.
# All tests produced the expected results.