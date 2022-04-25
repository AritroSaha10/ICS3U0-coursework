# -----------------------------------------------------------------------------
# Name:        Squared Magic
# Purpose:     A game where you have to solve a magic square as fast as possible
#
# Author:      Aritro Saha
# Created:     8-Mar-2022
# Updated:     10-Mar-2022
# -----------------------------------------------------------------------------

from random import randrange
from math import ceil, floor
from time import time


def printGrid(myGrid, maxNumLen):
    # Get length of row so we can print that many dashes
    rowSepLen = 1
    for num in myGrid[0]:
        numStr = str(num)

        # Calculate how much padding should be on the left of the line
        gridDisplayPaddingLeft = floor(maxNumLen / 2) - floor(len(numStr) / 2)

        # Calculate how much padding should be on the right of the line
        gridDisplayPaddingRight = ceil(maxNumLen / 2)

        # Add this length to the total length
        rowSepLen += gridDisplayPaddingLeft + \
            gridDisplayPaddingRight + len(numStr)

    # Actually print out the grid
    for row in myGrid:
        # Print row separators
        print('—' * rowSepLen)

        for num in row:
            numStr = ""

            # Don't print anything if it's 0
            if num == 0:
                numStr = "-"
            elif num < 0:
                # Something is very wrong, as there should never be any negative numbers at all
                print(
                    "Sorry, but an unexpected error occured. Please try running the program again.")
                exit()
            else:
                numStr = str(num)

            # Spacing for the left side of the line
            gridDisplayPaddingLeft = ' ' * \
                (floor(maxNumLen / 2) - floor(len(numStr) / 2))

            # Spacing for the right side of the line
            gridDisplayPaddingRight = ' ' * ceil(maxNumLen / 2)

            # Display the grid
            print(
                f"{numStr}{gridDisplayPaddingLeft}|{gridDisplayPaddingRight}", end='')

        # Add new line for new row
        print()

    # Add final divider
    print('—' * rowSepLen)


def checkGrid(myGrid, magicConst):
    gridSize = len(myGrid)
    gridCompleted = True

    # Loop through the rows to check if their sums match the magic const
    for rowIdx in range(gridSize):
        if sum(myGrid[rowIdx]) != magicConst:
            gridCompleted = False
            break
    else:
        # Loop through the columns to check if their sums match the magic const (only if the rows were completed)
        for colIdx in range(gridSize):
            col = [myGrid[i][colIdx] for i in range(gridSize)]
            if sum(col) != magicConst:
                gridCompleted = False
                break

    return gridCompleted


# Instruction screen
print("""
---- WELCOME TO SQUARED MAGIC! ----
Welcome to Squared Magic, a game where you solve a modified magic square puzzle as quickly as possible!

Instructions:
  1. You will first be asked about how large you want your square to be. This can be any value larger than 2. 
  2. After that, the magic square will be printed on the screen, as well as the sum that you should have in each row and column. 
  3. You will then be asked whether you want to add, change, or remove a number (input a, c, or r respectively), as well as the position. Note that you cannot remove the original number.
  4. If you are adding / changing, you will also be asked what number you'd like to change it to. Note that this number must be smaller than the sum previously stated.
  5. The action will be carried out. If this is a winning move, then you will be told so. Otherwise, the game continues until you complete the magic square.
  6. Once you complete the square, you'll be told your total time, as well as average time per move!

Good luck, and have fun!


      
""")

playAgainResp = ""
while playAgainResp != "No":
    # For formatting
    print()

    # Ask user for magic square size
    while (magicSquareSize := int(input("What would you like the size of your magic square to be? "))) <= 2:
        print("Please input a number larger than 2")
        print()

    # Generate the grid
    grid = [[0 for x in range(magicSquareSize)]
            for y in range(magicSquareSize)]

    # Calculate the magic constant
    magicConstant = magicSquareSize * (magicSquareSize ** 2 + 1) // 2

    # Generate a dictionary with numbers from 0 to the max allowed for frequency array
    gridNumFreqs = {i: 0 for i in range(magicConstant)}
    gridNumFreqs[0] = magicSquareSize ** 2

    # Place a random number in a random place in the grid
    startPos = (randrange(magicSquareSize), randrange(magicSquareSize))
    randStartNum = randrange(1, magicConstant // 2)
    grid[startPos[1]][startPos[0]] = randStartNum

    # Ensure placement is reflected in frequency array
    gridNumFreqs[randStartNum] = 1

    # Get max possible length of number to space out grid evenly
    maxNumLen = len(str(magicConstant)) + 2

    # Output magic sum
    print(f"Your magic sum: {str(magicConstant)}!")

    # Statistic vars
    timeSolveStart = time()
    moveCount = 0

    # Run as long as possible until grid is solved
    while not checkGrid(grid, magicConstant):
        # Print grid with some spacing
        printGrid(grid, maxNumLen)
        print()

        # Prompt user for whether they'd like to add, remove, or change
        addChangeRemoveChoice = input(
            "Would you like to add (a), change (c), or remove a number (r)? ")

        # Validate that they gave one of the accepted choices
        while addChangeRemoveChoice not in ["a", "c", "r"]:
            print("Please provide a valid option (Add -> a, Change -> c, Remove -> r).")
            print()
            addChangeRemoveChoice = input(
                "Would you like to add (a), change (c), or remove a number (r)? ")

        # Get the position to place the number
        rawCoordData = input(
            "What position would you like to change? (in format x y) ")

        # Validate that it is only 2 numbers
        while len(rawCoordData.split()) != 2:
            print("Please provide the appropriate number of numbers.")
            print()
            rawCoordData = input(
                "What position would you like to change? (in format x y) ")

        # Validate there are only numbers and no words / characters
        while not rawCoordData.replace(" ", "").isnumeric():
            print("Please provide integers.")
            print()
            rawCoordData = input(
                "What position would you like to change? (in format x y) ")

        # Convert input into actual numbers
        posX, posY = [int(coordinate) for coordinate in rawCoordData.split()]

        # Make sure they're not changing the starting number
        while (posX - 1, posY - 1) == startPos:
            print("You cannot replace the starting number. Please try another position.")
            print()
            rawCoordData = input(
                "What position would you like to change? (in format x y) ")
            posX, posY = [int(coordinate)
                          for coordinate in rawCoordData.split()]

        # Make sure the coordinate is in grid
        while posX > magicSquareSize or posY > magicSquareSize or posX <= 0 or posY <= 0:
            print(
                "The given position falls outside the grid. Please try another position.")
            print()
            rawCoordData = input(
                "What position would you like to change? (in format x y) ")
            posX, posY = [int(coordinate)
                          for coordinate in rawCoordData.split()]

        # Account for 0-based indices
        posX -= 1
        posY -= 1

        if addChangeRemoveChoice in ["a", "c"]:
            choiceExpanded = ""

            if addChangeRemoveChoice == "a":
                choiceExpanded = "add"
            elif addChangeRemoveChoice == "c":
                choiceExpanded = "change"

            # Request number
            newNumber = int(
                input(f"What number would you like to {choiceExpanded} in that position? "))

            # Check if new number is smaller than magic constant, loop until it is
            while newNumber >= magicConstant or newNumber <= 0:
                print(
                    f"Please make sure the number inputted is below the magic constant ({str(magicConstant)}), and larger than 0")
                print()
                newNumber = int(
                    input(f"What number would you like to {choiceExpanded} in that position? "))

            # Check if new number is unique
            while gridNumFreqs[newNumber] >= 1:
                print(f"That number has already been used. Please use a unique number")
                print()
                newNumber = int(
                    input(f"What number would you like to {choiceExpanded} in that position? "))

            # Change number in that position
            grid[posY][posX] = newNumber
            gridNumFreqs[newNumber] += 1

        elif addChangeRemoveChoice == "r":
            # Remove the number in that position
            gridNumFreqs[grid[posY][posX]] -= 1
            grid[posY][posX] = 0

        # Increment move count
        moveCount += 1

        # For spacing
        print("\n")
    else:
        # User completed, get end time
        endSolveTime = time()
        timeToComplete = round(endSolveTime - timeSolveStart, 2)
        timePerMove = timeToComplete / moveCount

        # Print stats
        print("Congrats! You completed the magic square.")
        print(f"Total time: {str(timeToComplete)}s")
        print(f"Total moves: {str(moveCount)} move(s)")
        print(f"Time per move: {str(timePerMove)}s")
        print()

        # Check if would like to play again
        playAgainResp = input("Would you like to play again? ")
        while playAgainResp not in ["Yes", "No"]:
            print("Please provide a proper response (Yes, No).")
            print()
            playAgainResp = input("Would you like to play again? ")
else:
    # User has decided not to continue
    print("See you later!")
