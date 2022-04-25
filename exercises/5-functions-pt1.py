# -----------------------------------------------------------------------------
# Name:        Functions Practice
# Purpose:     check out functions
#
# Author:      Aritro Saha
# Created:     11-Apr-2022
# Updated:     11-Apr-2022
# -----------------------------------------------------------------------------

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
