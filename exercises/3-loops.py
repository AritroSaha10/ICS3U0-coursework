# -----------------------------------------------------------------------------
# Name:        Loop Practice (main.py)
# Purpose:     Practice loops with factorials and summation
#
# Author:      Aritro Saha
# Created:     25-Feb-2022
# Updated:     25-Feb-2022
# -----------------------------------------------------------------------------

# Comment out the line below when you're done with the lesson code.
# import loops

# Define starting vars for factorial
number = int(input())
total = 1

if number < 1:
    print("Error.")
else:
    # Perform factorial calculation here (while loop)
    while number != 1:
        total *= number
        number -= 1

    print(total)

# Define starting vars for summation
begin = int(input())
end = int(input())

if begin > end:
    # Invalid input checking
    print("Error.")
else:
    total = 0
    # Perform addition calculation here (for loop)
    for num in range(begin, end + 1):
        total += num
    print(total)
