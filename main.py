# You have a group of friends coming to visit for your high school reunion,
# and you want to take them out to eat at a local restaurant.
# You aren't sure if any of them have dietary restrictions,
# but your restaurant choices are as follows:

# Joe's Gourmet Burgers --      Vegetarian: No      Vegan: No   Gluten-Free: No
# Main Street Pizza Company --  Vegetarian: Yes     Vegan: No   Gluten-Free: Yes
# Corner Cafe --                Vegetarian: Yes     Vegan: Yes  Gluten-Free: Yes
# Mama's Fine Italian --        Vegetarian: Yes     Vegan: No   Gluten-Free: No
# The Chef's Kitchen --         Vegetarian: Yes     Vegan: Yes  Gluten-Free: Yes

# Write a program that asks whether any members of your party are vegetarian, vegan, or gluten-free,
# and then displays only the restaurants that you may take the group to.

# ask the user if anyone in their party is a vegetarian
vegetarian = input("Is anyone in your party a vegetarian? (yes/no)\n").lower()

# input validation
# if the user doesn't respond with "yes" or "no", keep asking until they do
while (vegetarian != "yes" and vegetarian != "no"):
    print("Please respond with either 'yes' or 'no'.")
    vegetarian = input("Is anyone in your party a vegetarian? (yes/no)\n").lower()
    
# ask the user if anyone in their party is a vegan
vegan = input("Is anyone in your party a vegan? (yes/no)\n").lower()

# input validation
# if the user doesn't respond with "yes" or "no", keep asking until they do
while (vegan != "yes" and vegan != "no"):
    print("Please respond with either 'yes' or 'no'.")
    vegan = input("Is anyone in your party a vegan? (yes/no)\n").lower()

# ask the user if anyone in their party is a vegan
gluten_free = input("Is anyone in your party gluten-free? (yes/no)\n").lower()

# input validation
# if the user doesn't respond with "yes" or "no", keep asking until they do
while (gluten_free != "yes" and gluten_free != "no"):
    print("Please respond with either 'yes' or 'no'.")
    gluten_free = input("Is anyone in your party gluten-free? (yes/no)\n").lower()
    
print("\nHere are your restaurant choices:")

# if and else-if statements to determine output
# the following combinations of dietary restrictions lead to the same output
#       vegetarian, vegan, and gluten-free
#       vegan, gluten-free
#       vegetarian, vegan
#       vegan
if ((vegetarian == "yes" and vegan == "yes" and gluten_free == "yes") or (vegan == "yes" and gluten_free == "yes") or (vegetarian == "yes" and vegan == "yes") or (vegan == "yes")):
    print("Corner Cafe\nThe Chef's Kitchen")

# restaurants that are both vegetarian and gluten-free    
elif (vegetarian == "yes" and gluten_free == "yes"):
    print("Main Street Pizza Company\nCorner Cafe\nThe Chef's Kitchen")

# restaurants that are vegetarian
elif (vegetarian == "yes"):
    print("Main Street Pizza Company\nCorner Cafe\nMama's Fine Italian\nThe Chef's Kitchen")

# restaurants that are gluten-free
elif (gluten_free == "yes"):
    print("Main Street Pizza Company\nCorner Cafe\nThe Chef's Kitchen")

# restaurant options if we don't have any dietary restrictions to account for    
elif (vegetarian == "no" and vegan == "no" and gluten_free == "no"):
    print("Joe's Gourmet Burgers\nMain Street Pizza Company\nCorner Cafe\nMama's Fine Italian\nThe Chef's Kitchen")