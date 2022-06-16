#-----------------------------------------------------------------------------
# Name:        Tax Software (main.py)
# Purpose:     calculate the amount of federal income tax paid based on sources of income
#
# Author:      Aritro Saha
# Created:     28-Apr-2022
# Updated:     24-May-2022
#-----------------------------------------------------------------------------

from typing import Tuple, Union, Callable
import logging
import sys
import re

# Set up logging
logging.basicConfig(filename="log.txt", level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

def requireValidInput(inpStr: str, incorrectNote: str, checker: Callable[[str], bool]) -> str:
  '''
  Obtain valid input from a user.
  
  Obtain valid input from the user by repeatedly asking until their input is verified by a checker function. The input from the user will be returned.

  Parameters
  ----------
  inpStr : str
    The prompt shown to the user before collecting input.
  incorrectNote: str
    The prompt shown to the user when their input is invalid.
  checker: Callable[str, bool]
    A checker function that takes in the input string and returns a boolean depending on whether the input is valid or not
  
  Returns
  -------
  str
    The input from the user.

  Raises
	------
	TypeError
		If inpStr (str), incorrectNote (str), or checker (Callable[[str], bool]) is not the correct type
  '''

  logging.info(f"Running requireValidInput('{inpStr}', '{incorrectNote}', checker callable)")

  # Handle type errors
  if not isinstance(inpStr, str):
    logging.error("inpStr is not a string")
    raise TypeError("inpStr is not a string")
  elif not isinstance(incorrectNote, str):
    logging.error("incorrectNote is not a string")
    raise TypeError("incorrectNote is not a string")
  elif not callable(checker):
    logging.error("checker is not callable")
    raise TypeError("checker is not a callable")

  # Only exit once checker confirms
  while not checker(result := input(inpStr)):
    logging.debug("User did not provide proper input, reprompting.")
    print(incorrectNote)
    print()

  logging.info(f"Final result from requireValidInput: {result}")
  
  return result

def percentageToDecimal(percentage: Union[int, float]) -> float:
  '''
  Convert a percentage to a decimal value.
  
  Convert a percentage to a decimal value, given the percentage. If the percentage is smaller than 0, a ValueError will be raised. Otherwise, a decimal representation of the given percentage will be returned.

  Parameters
  ----------
  percentage : int or float
    The percentage to convert.
  
  Returns
  -------
  float
    A decimal representation of the given percentage, rounded to 5 decimal points.

  Raises
	------
	TypeError
		If percentage (int, float) is not the correct type
	ValueError
		If percentage is smaller than 0
  '''
  
  logging.info(f"Running percentageToDecimal({percentage})")

  # Handle type errors
  if not isinstance(percentage, (int, float)):
    logging.error("Percentage parameter is not an int or float")
    raise TypeError("Percentage parameter is not an int or float")

  # Handle value errors
  if percentage < 0:
    logging.error("Percentage cannot be below 0%")
    raise ValueError("Percentage cannot be below 0%")

  # Convert percentage to decimal
  decimalValue = percentage / 100

  logging.info(f"Decimal value of percentage: {decimalValue}")

  logging.debug(f"Returning decimal value of percentage rounded to 5 decimal points...")
  
  return round(decimalValue, 5)

# All the tax rates depending on type of income. 
# Taken from CRA's website.
# Value represents the tax rate as a decimal between 0 and 1
incomeTaxRates = {
  "Employment":                             percentageToDecimal(100),
  "Self-Employment":                        percentageToDecimal(100),
  "Eligible Dividends":                     percentageToDecimal(100),
  "Ineligible Dividends":                   percentageToDecimal(100),
  "Taxable Scholarships":                   percentageToDecimal(100),
  "Non-taxable Scholarships":               percentageToDecimal(0),
  "Rental Income":                          percentageToDecimal(38),
  "Capital Gains":                          percentageToDecimal(50),
  "Lottery Winnings":                       percentageToDecimal(0),
  "Gifts":                                  percentageToDecimal(0),
  "Inheritance":                            percentageToDecimal(0),
  "Other Taxable Income (EI, CERB, etc.)":  percentageToDecimal(100),
  "Other Non-Taxable Income":               percentageToDecimal(0)
}

# All of the federal tax brackets 
# Taken from CRA's website
# First value represents the max amount for the bracket
# Second value represents the amount of tax on that bracket
taxBrackets = [
  (49020,        percentageToDecimal(15)),      # First tax bracket:  15%   on income $49,020   or  less
  (98040,        percentageToDecimal(20.5)),    # Second tax bracket: 20.5% on income $49,020   to  $98,040
  (151978,       percentageToDecimal(26)),      # Third tax bracket:  26%   on income $98,040   to  $151,978
  (216511,       percentageToDecimal(29)),      # Fourth tax bracket: 29%   on income $151,978  to  $216,511
  (float('inf'), percentageToDecimal(33))       # Fifth tax bracket:  33%   on income more than     $216,511
]

def getTaxableAmount(incomeType: str, amount: Union[int, float]) -> Tuple[float, float]:
  '''
  Gets the taxable amount of income given the type and amount
  
  Determines the taxable amount of income, given the type of income, and the amount of income. If the income amount is smaller than 0, or the income type is not a key in incomeTaxRates, a ValueError will be raised. Otherwise, the tax rate and taxed amount will be returned in a tuple.

  Parameters
  ----------
  incomeType : str
    The type of income. The value must be a key in incomeTaxRates.
  amount : int or float
    The amount of this type of income.
  
  Returns
  -------
  tuple[float, float]
    A tuple including the taxable percentage and taxable amount, respectively.

  Raises
	------
	TypeError
		If incomeType (str) or amount (int, float) is not the correct type
	ValueError
		If incomeType is empty, not a key in incomeTaxRates, or the amount of income is below 0
  '''

  logging.info(f"Running getTaxableAmount('{incomeType}', {amount})")

  # Handle type exceptions
  if not isinstance(incomeType, str):
    logging.error("incomeType is not a string")
    raise TypeError("incomeType is not a string")

  if not isinstance(amount, (float, int)):
    logging.error("amount is not an int or float")
    raise TypeError("amount is not an int or float")

  # Handle value exceptions
  if amount < 0:
    logging.error("amount of income cannot be below 0")
    raise ValueError("amount of income cannot be below 0")

  if incomeType == "":
    logging.error("incomeType cannot be empty")
    raise ValueError("incomeType cannot be empty")

  # Only attempt to get the tax rate if the income type is recorded
  if incomeType in incomeTaxRates:
    taxRate = incomeTaxRates[incomeType]
    logging.info(f"Tax rate for {incomeType}: {taxRate}")
    
    taxedAmount = taxRate * amount
    logging.info(f"Taxable amount: {taxedAmount}")
    
    return taxRate, taxedAmount
  else:
    logging.error("Income type does not exist in incomeTaxRates when running getTaxableAmount")
    raise ValueError("Income type does not exist in incomeTaxRates when running getTaxableAmount")

def getTotalIncomeTax(taxableIncome: Union[int, float]) -> float:
  '''
  Gets the total amount of income tax charged on a certain amount of taxable income
  
  Gets the total amount of income tax charged on a certain amount of taxable income. If the income amount is smaller than 0, or the income type is not a key in incomeTaxRates, a ValueError will be raised. Otherwise, the tax rate and taxed amount will be returned in a tuple.

  Parameters
  ----------
  taxableIncome : int or float
    The amount of taxable income.
  
  Returns
  -------
  float
    The total amount of income tax charged on the given amount of taxable income, excluding deductions, rounded to 5 decimal points.

  Raises
	------
	TypeError
		If taxableIncome (int, float) is not the correct type
	ValueError
		If the amount of taxable income is below 0
  '''
  logging.info(f"Running getTaxableAmount({taxableIncome})")

  # Handle type exceptions
  if not isinstance(taxableIncome, (float, int)):
    logging.error("taxableIncome is not an int or float")
    raise TypeError("taxableIncome is not an int or float")

  # Handle value exceptions
  if taxableIncome < 0:
    logging.error("taxableIncome cannot be below 0")
    raise ValueError("taxableIncome cannot be below 0")

  incomeTax = 0
  
  # Loop through each bracket
  for i, (endOfBracket, rate) in enumerate(taxBrackets):
    # Get the amount of income that can be taxed under this bracket
    taxableIncomeUnderBracket = min(taxableIncome, endOfBracket)
  
    # Add to total income tax by multiplying the rate and amount of taxable income under this bracket
    incomeTax += taxableIncomeUnderBracket * rate
    
    logging.info(f"Bracket {i+1}: {taxableIncomeUnderBracket * rate}")
    
    # Subtract the income tax already charged from taxableIncome so it's not double counted
    taxableIncome -= taxableIncomeUnderBracket
  
    # No more income to tax
    if taxableIncome <= 0:
      logging.debug(f"No more income to tax, exiting loop...")
      break

  logging.info(f"Income tax calculated from getTotalIncomeTax: {incomeTax}")
  
  return round(incomeTax, 5)

logging.debug(f"Testing functions using assertions...")

# Assertions to test the percentageToDecimal function
assert percentageToDecimal(50) == 0.5, "50% is 0.5"
assert percentageToDecimal(25) == 0.25, "25% is 0.25"
assert percentageToDecimal(0.5) == 0.005, "0.5% is 0.005"
assert percentageToDecimal(83.9322) == 0.83932, "83.9322% rounded to 5 decimal points is 0.83932"
assert percentageToDecimal(43.2934) == 0.43293, "43.2934% rounded to 5 decimal points is 0.43293"
assert percentageToDecimal(10) == 0.1, "10% is 0.1"
assert percentageToDecimal(0.101) == 0.00101, "10% is 0.1"
assert percentageToDecimal(9.39) == 0.0939, "9.39% is 0.0939"

# Assertions to test the getTaxableAmount function
assert getTaxableAmount("Employment", 50000)[1] == 50000, "Employment income has a tax rate of 100%"
assert getTaxableAmount("Eligible Dividends", 50000)[1] == 50000, "Eligible dividends income has a tax rate of 100%"
assert getTaxableAmount("Capital Gains", 80000)[1] == 40000, "Capital gains income has a tax rate of 50%"
assert getTaxableAmount("Rental Income", 25394)[1] == 9649.72, "Rental income has a tax rate of 38%"
assert getTaxableAmount("Inheritance", 94203)[1] == 0, "Inheritance has a tax rate of 0%"
assert getTaxableAmount("Other Non-Taxable Income", 213123)[1] == 0, "Other Non-Taxable Income has a tax rate of 0%"
assert getTaxableAmount("Other Taxable Income (EI, CERB, etc.)", 1392)[1] == 1392, "Other Non-Taxable Income has a tax rate of 100%"
assert getTaxableAmount("Taxable Scholarships", 1030)[1] == 1030, "Taxable Scholarships have a tax rate of 100%"

# Assertions to test the getTotalIncomeTax function
assert getTotalIncomeTax(50000) == 7553.9, "Income tax on $50000 is $7553.9"
assert getTotalIncomeTax(0) == 0, "Income tax on $0 is $0"
assert getTotalIncomeTax(100000) == 17803.9, "Income tax on $100000 is $17803.9"
assert getTotalIncomeTax(394034) == 94514.32, "Income tax on $50000, rounded to 5 decimal points, is $94514.32"
assert getTotalIncomeTax(3039281928) == 1002922658.74, "Income tax on $3039281928, rounded to 5 decimal points, is $1002922658.74"
assert getTotalIncomeTax(1) == 0.15, "Income tax on $1 is $0.15"
assert getTotalIncomeTax(192032) == 39143.92, "Income tax on $192032 is $39143.92"
assert getTotalIncomeTax(250) == 37.5, "Income tax on $250 is $37.5"

logging.debug(f"Done testing functions!")

if __name__ == "__main__":
  taxableIncome = 0
  totalIncome = 0
  
  logging.debug("Program starting...")
  
  print("-- Federal Income Tax Calculator --")
  print("Calculate a rough estimate of the amount of income tax that you need to pay to the federal government! Note that deductions are not covered in this program.")
  print("-----------------------------------------")
  
  logging.debug("Entering main loop...")
  
  recordingTypesOfIncome = True
  while recordingTypesOfIncome:
    # Output all income types and their indices
    print("All types of income: ")
    for i, incomeType in enumerate(incomeTaxRates):
      print(f"{i+1}: {incomeType}")
  
    logging.debug("Getting type of income to add from user (no type conversion yet)...")

    # Get which income type the user wants
    checkIfValidIdx = lambda myStr: (myStr == "q") or (myStr.isnumeric() and (idx := int(myStr)) < len(incomeTaxRates) + 1 and idx > 0)
    
    incomeTypeIdxRaw = requireValidInput(
      """What income would you like to file (input the index, or q to quit)? """, 
      "Please provide either a number in the range or q to quit.", 
      checkIfValidIdx
    )
  
    # Quit if they type in "q"
    if incomeTypeIdxRaw == "q":
      recordingTypesOfIncome = False
      logging.debug("User is done inputting all income sources")
      break

    logging.info(f"User chose index of '{incomeTypeIdxRaw}', converting to integer...")

    # Convert to integer
    incomeTypeIdx = int(incomeTypeIdxRaw) - 1
      
    # Get actual income type from dictionary
    incomeType = list(incomeTaxRates.keys())[incomeTypeIdx]
  
    logging.info(f"Actual income type: {incomeType}")
    
    # Ask how much income of that type
    logging.debug("Getting amount of income under that type...")

    # Lambda to check whether its a dollar
    checkIfDollar = lambda myStr: re.sub(r"[ ,.]", "", myStr).isnumeric() and myStr.count(".") <= 1
    
    rawIncomeStr = requireValidInput(
      f"How much of '{incomeType}' income do you have? $", 
      "Please input a valid dollar amount.", 
      checkIfDollar
    )
  
    logging.info(f"Raw income amount from user (string): {rawIncomeStr}")
    
    # Clean string before converting to float
    logging.debug("Cleaning input from user...")
    rawIncomeStr = re.sub(r"[ ,]", "", rawIncomeStr)
    logging.debug(f"Cleaned income amount from user (not converted to float yet): {rawIncomeStr}")
  
    # Convert to float, no error checking needed as input has been validated
    rawIncome = float(rawIncomeStr)
  
    # Add to total income
    logging.info(f"Raw income as float: {rawIncome}")
    totalIncome += rawIncome
    logging.info(f"New total income: {totalIncome}")
  
    # Get the amount taxable, and how much that is
    logging.debug(f"Getting the taxable percentage and taxable income using getTaxableAmount, with params incomeType='{incomeType}' and amount={rawIncome}")
  
    try:
      taxRate, taxableAmount = getTaxableAmount(incomeType, rawIncome)
    except Exception as e:
      logging.error(
        f"""Something went wrong while 
        getting the taxable rate and 
        amount: {str(e)}"""
      )
      print(
        f"""Something went wrong while getting
        the taxable rate and amount: {str(e)}"""
      )
      sys.exit(1)
  
    logging.info(f"Tax rate of income: {taxRate}")
    logging.info(f"Taxable amount: {taxableAmount}")
  
    # Prepare for displaying to user
    taxableAmountRounded = round(taxableAmount, 2)
    taxRate = taxRate * 100 # Convert to percentage
    
    print(f"${taxableAmountRounded:,.2f} of the amount, or {taxRate:.2f}% of it will count as taxable income.")
  
    # Add to total
    taxableIncome += taxableAmount
  
    print()
    print()
  
  print()
  print()
  
  print(f"Total taxable income: ${taxableIncome:,.2f}")
  logging.info(f"Total taxable income: {taxableIncome}")
  
  # Calculate amount of income tax
  try:
    incomeTax = getTotalIncomeTax(taxableIncome)
  except Exception as e:
    logging.error(f"Something went wrong while calculating income tax: {str(e)}")
    print(f"Something went wrong while calculating income tax: {str(e)}")
    sys.exit(1)
  
  # Display total income tax without any deductions
  print(f"Total income tax (w/o Basic Personal Amount): ${incomeTax:,.2f}")
  
  totalDeductions = 0
  # Account for BPA
  if taxableIncome <= 151978:
    totalDeductions += 13808
  elif taxableIncome >= 216511:
    totalDeductions += 12421
  else:
    # Federal Worksheet doesn't tell you what the basic personal amount is for incomes between 151K and 216K, just tells you to "use the federal worksheet"...
    # Due to that, this is probably incorrect, as it's just an average between the two. 
    totalDeductions += 13114.5
  
  logging.info(f"Deductions after Basic Personal Amount: {totalDeductions}")
  
  # Federal non-refundable tax credit rate is 15%
  incomeTax -= totalDeductions * 0.15
  
  # Make sure it doesn't drop below 0
  incomeTax = max(incomeTax, 0)
  
  logging.info(f"Total amount of income tax: {incomeTax}")
  
  # Round to 2 decimal points
  roundedIncomeTax = round(incomeTax, 2)
  
  # Print final income tax
  print(f"Total income tax (w/ BPA deduction): ${roundedIncomeTax:,.2f}")
  
  print()
  
  # What if they had earned 30% more?
  logging.debug("Asking user if they want to see their tax if they earned 30% more...")
  shouldEarnMore = input("Would you like to know your income tax if you earned 30% more in taxable income? (yes/no) ").lower()
  logging.info(f"Response to whether they would like to see their tax if they earned 30% more: '{shouldEarnMore}'")
  
  print()
  
  # Only run if they want to
  if shouldEarnMore == "yes":
    logging.info("Calculating income tax with 30% more taxable income...")
    # Reset variables
    incomeTax = 0
    totalDeductions = 0
    roundedIncomeTax = 0
  
    taxableIncome *= 1.3
    print(f"30% added to current taxable income: ${taxableIncome:,.2f}")
    logging.info(f"30% added to taxable income: {taxableIncome}")
  
    # Calculate amount of income tax
    try:
      incomeTax = getTotalIncomeTax(taxableIncome)
    except Exception as e:
      logging.error(f"Something went wrong while calculating income tax: {str(e)}")
      print(f"Something went wrong while calculating income tax: {str(e)}")
      sys.exit(1)
    
    # Display total income tax without any deductions
    print(f"Total income tax (w/30% extra income, w/o Basic Personal Amount): ${incomeTax:,.2f}")
    logging.info(f"Total income tax (w/30% extra income, w/o Basic Personal Amount): ${incomeTax}")
    
    totalDeductions = 0
    # Account for BPA
    if taxableIncome <= 151978:
      totalDeductions += 13808
    elif taxableIncome >= 216511:
      totalDeductions += 12421
    else:
      # Federal Worksheet doesn't tell you what the basic personal amount is for incomes between 151K and 216K, just tells you to "use the federal worksheet"...
      # Due to that, this is probably incorrect, as it's just an average between the two. 
      totalDeductions += 13114.5
    
    logging.info(f"Deductions after Basic Personal Amount: {totalDeductions}")
    
    # Federal non-refundable tax credit rate is 15%
    incomeTax -= totalDeductions * 0.15
    
    # Make sure it doesn't drop below 0
    incomeTax = max(incomeTax, 0)
    
    logging.info(f"Total amount of income tax (w/30% more income): {incomeTax}")
    
    # Round to 2 decimal points
    roundedIncomeTax = round(incomeTax, 2)
    
    # Print final income tax
    print(f"Total income tax (w/ BPA deduction & 30% more income): ${roundedIncomeTax:,.2f}")

logging.debug("Program has ended.")
