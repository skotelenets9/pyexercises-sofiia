"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In: Campaign name, advertising platform, and budget. 
# 2. Process: The program asks the user for campaign details and saves them to a CSV file.
# It adds new entries without deleting previous ones and checks that the budget is valid.


# 3. Out, file name and columns: marketing_campaigns.csv
# Columns : Campaign, Platform, Budget.

# 4. Why these columns, and what this file is for:
# I chose these columns to track marketing expenses.
# With 200 entries, I could compare advertising platforms, calculate total spending, and analyse campaign budgets.

# Your code below
import csv
import os

# Ask the user for campaign information
campaign = input("Enter campaign name: ").strip()
platform = input("Enter advertising platform: ").strip()

# Make sure the campaign name and platform are not empty
while not campaign:
    campaign = input("Enter a campaign name: ").strip()

while not platform:
    platform = input("Enter a platform: ").strip()

# Check that the budget is a valid number
while True:
    try:
        budget = float(input("Enter budget in euros: "))
        if budget >= 0:
            break
        print("Budget cannot be negative.")
    except ValueError:
        print("Please enter a valid number.")

# Check whether the CSV needs a header
filename = "marketing_campaigns.csv"
new_file = not os.path.exists(filename) or os.path.getsize(filename) == 0

# Add the campaign to the CSV file
with open(filename, "a", newline="") as file:
    writer = csv.writer(file)

    if new_file:
        writer.writerow(["Campaign", "Platform", "Budget"])

    writer.writerow([campaign, platform, budget])

print("Campaign saved successfully!")

# Test: I ran the program three times with different campaign details.
# The CSV contains three entries and one header.
# Previous entries were not overwritten.