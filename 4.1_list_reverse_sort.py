"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of marketing budgets in euros.
# 2. Process:The program rearranges the budgets in four ways. 
# 3. Out: Four diffrent orders and an original unchanged list.
# 4. My four orders, and which ones modify the original:
# Original order: Keeps the budgets as initially entered.
# Ascending order: From smallest to largest, using sorted().
# Descending order: From largest to smallest, using sorted().
# Reversed order: Displays the budgets in reverse order.
# None of these operations modify the original list.

# Your code below
budgets = [500, 1200, 800, 1500, 600, 2000, 900, 1100]
#Original list: 
print("Original order:", budgets)
#Ascending : 
print("Ascending order:", sorted(budgets))
#Descending order: 
print("Descending order:", sorted(budgets, reverse=True))
#Reversed order: 
print("Reversed order", budgets[::-1])
#The original unchanged:
print("Original list at the end:", budgets)

# Test: I compared the original list with the final list.
# The eight budgets remained in the same order.
# sorted() creates a new list without modifying the original.
# Reversing with [::-1] also creates a new list.
# The original list was preserved.