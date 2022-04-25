# -----------------------------------------------------------------------------
# Name:        Exceptions Practice
# Purpose:     Practice proper exception usage
#
# Author:      Aritro Saha
# Created:     21-Apr-2022
# Updated:     21-Apr-2022
# -----------------------------------------------------------------------------

litresPerKm = 0.077  # 7.7 L per 100KM, Civic driving in city

# Canadian gas price, taken from this https://www.globalpetrolprices.com/gasoline_prices/
dollarPerLitre = 1.903


def milesToKm(distance):
    '''
    Converts units from miles to kilometres

    Converts a distance from miles to kilometres. If the distance is smaller than 0, return "Error.". Otherwise, return the distance in kilometres, rounded to 2 decimal points. 

    Parameters
    ----------
    distance : int or float
      The distance to be converted in miles

    Returns
    -------
    float
      The distance converted to kilometres, rounded to 2 decimal points.

    Raises
          ------
          TypeError
                  If distance (int, float) is not the correct type
          ValueError
                  If distance is negative
    '''

    # Ensure types match
    if not isinstance(distance, (int, float)):
        raise TypeError("Distance parameter is not int/float.")

    # Distance cannot be smaller than 0
    if distance < 0:
        raise ValueError("Distance parameter is negative.")

    # 1.60934 is the unit conversion from miles to kilometres
    return round(1.60934 * distance, 2)

# Reduce the given price by the given discount, rounded to decimal places


def saleCalc(price, discount):
    '''
    Calculate a discounted price.

    Calculate the final price after a discount. If price or discount is smaller than 0, or the discount is over 100%, "Error." will be returned. Otherwise, return the discounted price rounded to 2 decimal places.

    Parameters
    ----------
    price : int, float
      The original price of the item
    discount : int, float
      The discount to apply to the item, as a percentage

    Returns
    -------
    float
      The discounted price rounded to 2 decimal places.

    Raises
          ------
          TypeError
                  If price (int, float) or discount (int, float) is not the correct type
          ValueError
                  If the price or discount is negative, or the discount is larger than 100
    '''

    # Ensure types match
    if not isinstance(price, (int, float)):
        raise TypeError("Price parameter is not int or float.")

    if not isinstance(discount, (int, float)):
        raise TypeError("Discount parameter is not int or float.")

    # Raise error if parameters do not follow restrictions
    if price < 0 or discount < 0:
        raise ValueError("Price or discount parameter is negative.")

    if discount >= 100:
        raise ValueError("Discount parameter larger than 100%.")

    # Subtract the given percent of the price
    discountedPrice = price - (price * (discount / 100))

    # Return the discounted price rounded to 2 decimal places
    return round(discountedPrice, 2)


# Test the milesToKm to ensure it works as intended
assert milesToKm(1) == 1.61, "1 mile (rounded to 2 decimal points) is 1.61km"
assert milesToKm(0) == 0, "0 miles is 0km"
assert milesToKm(
    1923) == 3094.76, "1923 miles (rounded to 2 decimal points) is 3094.76km"
# assert milesToKm(-1) == "Error.", "Impossible to convert negative distances"

# Test the saleCalc to ensure it works as intended
assert saleCalc(
    100, 50) == 50, "50% off of $100 results in a final price of $50"
assert saleCalc(
    20, 23) == 15.4, "23% off of $20 results in a final price of $15.4"
# assert saleCalc(-100, 50) == "Error.", "Impossible to deduct from a negative pricce"
# assert saleCalc(100, -50) == "Error.", "Impossible to have a negative discount"
# assert saleCalc(100, 120) == "Error.", "Impossible to have a discount more than 100%"


# Define all of the stores, each with their own distance values in miles, as well as the items they carry.
stores = {
    "NoFrills": {
        "distance": 5,  # in miles
        "food": {
            "Apples with 15% Discount": saleCalc(2, 0.15),  # in dollars
            "Bananas": 3,  # in dollars
            "Whole Chicken with 20% Discount": saleCalc(15, 0.2),  # in dollars
            "Celery": 0.7  # in dollars
        }
    },
    "Walmart": {
        "distance": 7,  # in miles
        "food": {
            "Apples": 3,  # in dollars
            "Bananas": 2,  # in dollars
            "Whole Chicken with 10% Discount": saleCalc(13, 0.1),  # in dollars
            "Celery": 2  # in dollars
        }
    },
    "Whole Foods": {
        "distance": 15,  # in miles
        "food": {
            "Organic Apples": 4.5,  # in dollars
            "Organic Bananas": 6.7,  # in dollars
            "Free-run Eggs": 7,  # in dollars
            "Organic Juice": 5  # in dollars
        }
    },
    "Costco": {
        "distance": 12,  # in miles
        "food": {
            "Apple": 0.6,  # in dollars
            "Banana": 0.2,  # in dollars
            # in dollars
            "Rotisserie Chicken with 12% Discount": saleCalc(30, 0.12),
            "Celery": 0.7,  # in dollars
            "Laptop": 640  # in dollars
        }
    }
}

# Print the header of the program
print("Grocery Trip Simulator")
print()
print()

# Print each store with a number beside it
print("Which store would you like to go to? ")
for i, (key, val) in enumerate(stores.items()):
    print(i + 1, key)

# Get the store chosen by making the user type in the index from before
try:
    chosenStoreIdx = int(input("Type the number here: ")) - 1
except Exception as e:
    print("Something went wrong:", str(e))
else:
    try:
        chosenStore = list(stores.keys())[chosenStoreIdx]
        chosenStoreData = stores[chosenStore]
    except Exception as e:
        print("Something went wrong:", e)
    else:
        # Separator line
        print()

        # Calculate driving distance and price (rounded to 2 decimal places)
        try:
            kmToDrive = milesToKm(chosenStoreData["distance"])
        except Exception as e:
            print("Something went wrong:", str(e))
        else:
            gasNeeded = round(litresPerKm * kmToDrive, 2)
            gasMoney = round(gasNeeded * dollarPerLitre, 2)

            # Display driving info
            print(
                f"Driving to {chosenStore} will take {chosenStoreData['distance']} miles, or {kmToDrive} kilometres")
            print(
                f"You have a Honda Civic, so you will be using {gasNeeded}L of fuel, which equates to ${gasMoney} in gas money.")

            # Separator
            print()

            # Display all items to buy
            print(f"You are now at {chosenStore}! Buy a few things:")
            for i, (name, price) in enumerate(chosenStoreData["food"].items()):
                print(f"{i + 1} -> {name}: ${price}")

            # Get all of the food names from the chosen store
            allFoods = list(chosenStoreData['food'].keys())

            # Allow user to input things to buy as "1 2 3 1"
            thingsToBuyRaw = input(
                f"What would you like to buy?\nInput multiple space-separated integers representing what you'd like to buy (ex. 1 1 1 1 to buy four \'{allFoods[0]}\'): ")

            try:
                # Turn raw input into each food name
                thingsToBuyCleaned = [
                    allFoods[int(num) - 1] for num in thingsToBuyRaw.split(" ")]

                # Make frequency array from the latest input
                thingsToBuyFreq = {}
                for thing in thingsToBuyCleaned:
                    if thing in thingsToBuyFreq:
                        thingsToBuyFreq[thing] += 1
                    else:
                        thingsToBuyFreq[thing] = 1

                # Calculate sub total by multiplying frequency of each item with their price
                grocerySubtotal = 0
                for item, freq in thingsToBuyFreq.items():
                    grocerySubtotal += freq * chosenStoreData["food"][item]
            except Exception as e:
                print("Something went wrong:", str(e))
            else:
                # Add tax and 15% discount, and round to 2 decimal places
                groceryTotal = round(saleCalc(grocerySubtotal, 15) * 1.13, 2)

                # Display subtotal and total
                print()
                print(f"Your subtotal: ${round(grocerySubtotal, 2)}")
                print(f"Final total (w/tax and 15% coupon): ${groceryTotal}")

                # Separator
                print()

                # Let the user know that their gas cost will be doubled
                print(
                    f"You are now going back home, which means you will be using the same amount of gas again.")

                # Separator
                print()

                try:
                    # Ask for any more miles they may have driven
                    extraDrivenMiles = float(input(
                        "Input any more driving (in miles) that you may have done while on the trip: "))
                except Exception as e:
                    print("Something went wrong:", e)
                else:
                    # Calculate driving distance in KM and price
                    try:
                        extraKmDrive = milesToKm(extraDrivenMiles)
                    except Exception as e:
                        print("Something went wrong:", e)
                    else:
                        gasNeededExtra = round(litresPerKm * extraKmDrive, 2)
                        gasMoneyExtra = round(
                            gasNeededExtra * dollarPerLitre, 2)

                        # Display all money spent
                        print(
                            f"Your trip is done! Total amount spent (incl. gas): ${round(groceryTotal + gasMoney * 2 + gasMoneyExtra, 2)}")
