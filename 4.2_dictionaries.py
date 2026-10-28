"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:Info about a music marketing campaign.
# 2. Process:The program creates a dictionary, reads a field, updates a value, removes a field and displays remaining fields. 
# 3. Out: The capaign info after changes.
# 4. My object, my five fields, and why those:
#My object is a music marketing campaign.
# Name: identifies the campaign.
# Artist: identifies who is being promoted.
# Budget: tracks marketing expenses.
# Platform: identifies the advertising channel.
# Status: tracks campaign progress.

# Your code below
campaign = {
    "name": "New Album Launch",
    "artist": "Drake",
    "budget": 8900,
    "platform": "Instagram",
    "status": "Planned"
}
#Read one field: 
print("Campaign name:", campaign["name"])

#Change:
campaign["budget"] = 8000
print("Updated budget:", campaign["budget"])

# Remove a field
del campaign["status"]

# Display all remaining fields
for key, value in campaign.items():
    print(key, ":", value)

print("Audience:", campaign.get("audience", "Not available"))

# Test: Accessing a missing field with [] caused a KeyError.
# Using .get() displayed "Not available" instead.
# The program now handles missing fields without crashing.