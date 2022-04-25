# -----------------------------------------------------------------------------
# Name:        Grocery Dictionary
# Purpose:     Creates a dictionary for groceries
#
# Author:      Aritro Saha
# Created:     3-Mar-2022
# Updated:     3-Mar-2022
# -----------------------------------------------------------------------------

groceryDict = {}

# Use input() and while loop to add key/value until '!' entered
while (foodName := input()) != "!":
    # Get quantity
    quantity = int(input())
    if foodName not in groceryDict:
        # If key doesn't exist, add the key/value
        groceryDict[foodName] = quantity
    else:
        # If key exists, increment the value (int)
        groceryDict[foodName] += quantity

# Print dictionary
print(groceryDict)

# Take input(), remove from groceryDict if exists
if (itemToRemove := input()) in groceryDict:
    del groceryDict[itemToRemove]

# Calculate and print the sum of values
quantitySum = sum([quantity for quantity in groceryDict.values()])
print(quantitySum)
