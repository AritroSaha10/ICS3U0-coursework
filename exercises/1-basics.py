#-----------------------------------------------------------------------------
# Name:        Reviewing the Basics
# Purpose:     Reviews the basics of python (input, math, print)
#
# Author:      Aritro Saha
# Created:     22-Feb-2022
# Updated:     22-Feb-2022
#-----------------------------------------------------------------------------

# This line will run the basics file (my example).
# import basics

# Start writing your code here! (and make sure to modify the header above!)

# Get number from user
yourNumber = int(input("Give me a number: "))

# Transform it to be better
betterNumber = (yourNumber + 10) / 2

# Display better number to user
print("Your number (but better): " + str(betterNumber))


# Get another number to transform
yourNumber2 = int(input("Give me another number: "))

# Make the number worse
worseNumber = (yourNumber - 20) // 3

# Display worse number
print("Your number (but worse): " + str(worseNumber))


# Get another number to transform
yourNumber3 = int(input("Give me yet another number: "))

# Make the number the same
yourNumber3 += 10
yourNumber3 -= 10

# Display the same number
print("Your number (but the same): " + str(yourNumber3))


# Get yet another number to transform
yourNumber4 = int(input("Give me ANOTHER number (this is the 2nd last time): "))

# Transform the number again
yourNumber4 = (yourNumber4 % 34) // 3 - 10

# Display transformed number
print("Your number but changed to be the best number: " + str(yourNumber4))


# Get the last number to transform
yourNumber5 = int(input("Just one more number (last time): "))

# Transform the age to be useful
yourNumber5 = (10 / yourNumber5) * 23 - 100

# Display transformed number to use
print("Your number but changed to be super useful: " + str(yourNumber5))