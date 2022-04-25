# -----------------------------------------------------------------------------
# Name:        Grocery List
# Purpose:     Creates and handles a grocery list using python list methods
#
# Author:      Aritro Saha
# Created:     1-Mar-2022
# Updated:     1-Mar-2022
# -----------------------------------------------------------------------------

# Lesson files
# import lists
# import list_methods

groceryList = []

# Use while loop to use input() to fill list
# Items are added only if not already in list
# Loop should stop when '!' is entered
while (newItem := input()) != "!":
    if newItem not in groceryList:
        groceryList.append(newItem)

# Sort and print the list
groceryList.sort()
print(groceryList)

# Print 3rd item, then 3rd LAST item
print(groceryList[2])
print(groceryList[-3])

# Print slice of 4th through 6th item
print(groceryList[3:6])

# Print same slice BACKWARDS
print(groceryList[5:2:-1])

# Remove last item
groceryList.pop()

# Take input(), remove that item if it exists
if (itemToRemove := input()) in groceryList:
    groceryList.remove(itemToRemove)

# Print List
print(groceryList)

# DO NOT CHANGE THIS LIST
intList = [5, 8, -10, 3, 18, 22, 1, 71]

# If item in list is odd, multiply by 2
modifiedIntList = [
    integer * 2 if integer % 2 == 1 else integer
    for integer in intList
]

# Print list
print(modifiedIntList)
