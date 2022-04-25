# -----------------------------------------------------------------------------
# Name:        Grade Checker
# Purpose:     Returns feedback given a percentage grade
#
# Author:      Aritro Saha
# Created:     23-Feb-2022
# Updated:     23-Feb-2022
# -----------------------------------------------------------------------------

# Comment out the line below when you're done with the lesson code.
#import conditionals

# You will check the 'grade' variable using if/elif/else statements.
# Your output must EXACTLY MATCH what is requested in TASK.md

grade = int(input("What is your grade? "))

# First check whether grade is valid or not
if grade <= 100 and grade >= 0:
    # Step down depending on grade
    if grade >= 80:
        print("Exceeding Expectations.")
    elif grade >= 70:
        print("Meeting Expectations.")
    elif grade >= 50:
        print("Needs Improvement.")
    else:
        # Grade is lower than 50
        print("Not Passing.")
else:
    print("Invalid Grade.")
