# TODO
from cs50 import get_int

# necessary variables
creditCardNumber = get_int("Card number: ")
firstSum = 0
secondSum = 0
cardStructure = "INVALID"
quantityOfDigits = 0
temp = 0

# Define how many digits the cardNumber has
for i in [15, 14, 13, 12]:
    if int(creditCardNumber / pow(10, i)) > 0:
        quantityOfDigits = i
        break
# Temporary integer to define card structure
if quantityOfDigits >= 12:
    cardStructureDefinition = int(creditCardNumber / pow(10, quantityOfDigits - 1))
else:
    cardStructureDefinition = 0

# Define card by its structure
if int(cardStructureDefinition / 10) >= 1 and int(cardStructureDefinition / 10) <= 9:
    if cardStructureDefinition in [34, 37]:
        cardStructure = "AMEX"
    elif cardStructureDefinition in [51, 52, 53, 54, 55, 22]:
        cardStructure = "MASTERCARD"
    elif int(cardStructureDefinition / 10) == 4:
        cardStructure = "VISA"

    # Verify of validity
    i = quantityOfDigits
    while i >= 0:
        if i % 2 == 0:
            secondSum += int(creditCardNumber / pow(10, i))
        else:
            temp = int(creditCardNumber / pow(10, i)) * 2
            if temp >= 10:
                firstSum += int(temp / 10) + temp % 10
            else:
                firstSum += temp
        creditCardNumber = creditCardNumber % pow(10, i)
        i -= 1
    if (firstSum + secondSum) % 10 != 0:
        cardStructure = "INVALID"

# Print out the result
print(cardStructure)