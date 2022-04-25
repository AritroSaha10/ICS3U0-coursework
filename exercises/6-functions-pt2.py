# -----------------------------------------------------------------------------
# Name:        Functions 2
# Purpose:     makes multiple calls of two functions in a meaningful way
#
# Author:      Aritro Saha
# Created:     12-Apr-2022
# Updated:     12-Apr-2022
# -----------------------------------------------------------------------------

litresPerKm = 0.077  # 7.7 L per 100KM, Civic driving in city
# taken from this https://www.globalpetrolprices.com/gasoline_prices/
dollarPerLitre = 1.903

# Convert a distance in miles to kilometres


def milesToKm(distance):
    if distance < 0:
        return "Error."
    return round(1.60934 * distance, 2)

# Reduce the given price by the given discount, rounded to decimal places


def saleCalc(price, discount):
    if price < 0 or discount < 0 or discount >= 100:
        return "Error."

    discountedPrice = price - (price * (discount / 100))

    return round(discountedPrice, 2)


stores = {
    "NoFrills": {
        "distance": 5,
        "food": {
            "Apples with 15% Discount": saleCalc(2, 0.15),
            "Bananas": 3,
            "Whole Chicken with 20% Discount": saleCalc(15, 0.2),
            "Celery": 0.7
        }
    },
    "Walmart": {
        "distance": 7,
        "food": {
            "Apples": 3,
            "Bananas": 2,
            "Whole Chicken with 10% Discount": saleCalc(13, 0.1),
            "Celery": 2
        }
    },
    "Whole Foods": {
        "distance": 15,
        "food": {
            "Organic Apples": 4.5,
            "Organic Bananas": 6.7,
            "Free-run Eggs": 7,
            "Organic Juice": 5
        }
    },
    "Costco": {
        "distance": 12,
        "food": {
            "Apple": 0.6,
            "Banana": 0.2,
            "Rotisserie Chicken with 12% Discount": saleCalc(30, 0.12),
            "Celery": 0.7,
            "Laptop": 640
        }
    }
}

# Write some code that makes MULTIPLE CALLS of at least one of the functions, producing different results and being used in a meaningful way.
print("Grocery Trip Simulator")
print()
print()

# Print each store with a number beside it
print("Which store would you like to go to? ")
for i, (key, val) in enumerate(stores.items()):
    print(i + 1, key)

# Get the store chosen by typing in the number
chosenStoreIdx = int(input("Type the number here: ")) - 1
chosenStore = list(stores.keys())[chosenStoreIdx]
chosenStoreData = stores[chosenStore]

print()

# Calculate driving distance and price
kmToDrive = milesToKm(chosenStoreData["distance"])
gasNeeded = round(litresPerKm * kmToDrive, 2)
gasMoney = round(gasNeeded * dollarPerLitre, 2)

# Display driving info
print(
    f"Driving to NoFrills will take {chosenStoreData['distance']} miles, or {kmToDrive} kilometres")
print(
    f"You have a Honda Civic, so you will be using {gasNeeded}L of fuel, which equates to ${gasMoney} in gas money.")

print()

# Display all items to buy
print(f"You are now at {chosenStore}! Buy a few things:")
for i, (name, price) in enumerate(chosenStoreData["food"].items()):
    print(f"{i + 1} -> {name}: ${price}")

allFoods = list(chosenStoreData['food'].keys())

# Allow user to input things to buy as "1 2 3 1"
thingsToBuyRaw = input(
    f"What would you like to buy?\nInput multiple space-separated integers representing what you'd like to buy (ex. 1 1 1 1 to buy four \'{allFoods[0]}\'): ")

# Turn string into list of nums
thingsToBuyCleaned = [allFoods[int(num) - 1]
                      for num in thingsToBuyRaw.split(" ")]

# Make frequency array from this list`
thingsToBuyFreq = {}
for thing in thingsToBuyCleaned:
    if thing in thingsToBuyFreq:
        thingsToBuyFreq[thing] += 1
    else:
        thingsToBuyFreq[thing] = 1

# Calculate sub total
grocerySubtotal = 0
for item, freq in thingsToBuyFreq.items():
    grocerySubtotal += freq * chosenStoreData["food"][item]

# Add tax and 15% coupon
groceryTotal = round(saleCalc(grocerySubtotal, 15) * 1.13, 2)

# Display subtotal and total
print()
print(f"Your subtotal: ${grocerySubtotal}")
print(f"Final total (w/tax and 15% coupon): ${groceryTotal}")

print()

print(f"You are now going back home, which means you will be using the same amount of gas again.")

print()

extraDrivenMiles = float(input(
    "Input any more driving (in miles) that you may have done while on the trip: "))

# Calculate driving distance and price
extraKmDrive = milesToKm(extraDrivenMiles)
gasNeededExtra = round(litresPerKm * extraKmDrive, 2)
gasMoneyExtra = round(gasNeededExtra * dollarPerLitre, 2)

# Display all money spent
print(
    f"Your trip is done! Total amount spent (incl. gas): ${round(groceryTotal + gasMoney * 2 + gasMoneyExtra, 2)}")
