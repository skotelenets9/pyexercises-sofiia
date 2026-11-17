"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - Some names are written in uppercase and others in lowercase.
# - Some lines have extra spaces at the beginning.
# - There are empty lines between names.
# - Capitalization is inconsistent within names.

# 1. In: A text file called names.txt containing people's names.
# 2. Process, problem by problem:
# Remove empty lines.
# Remove extra spaces using strip()
# Capitalize names consistently using title()
# Sort names alphabetically by last name. 

# 3. Out: A new file called sorted_names.txt containing cleaned names sorted by last name.

# 4. How I decide which word is the last name:
# I assume the last word og each name is the last name.
# I use split()[-1] to find it and sort alphabetically.


# Your code below
# Read the original file
with open("names.txt", "r", encoding="utf-8") as file:
    names = file.readlines()

# Clean the names
cleaned_names = []

for name in names:
    clean_name = " ".join(name.strip().split()).title()

    if clean_name:
        cleaned_names.append(clean_name)

# Sort by last name
cleaned_names.sort(key=lambda name: name.split()[-1].lower())

# Save the cleaned names in a new file
with open("sorted_names.txt", "w", encoding="utf-8") as file:
    for name in cleaned_names:
        file.write(name + "\n")

print("Names cleaned and saved successfully!")

# Test: names.txt contained 10 lines, including 2 empty lines.
# The output file contains 8 cleaned names.
# The first name in sorted order is Margaret Hamilton.
# The last name in sorted order is Alan Turing.
# The original names.txt file was not modified.