#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    long creditCardNumber = 0;
    int quantityOfDigits = 0;
    int firstSum = 0, secondSum = 0, temp = 0;
    string cardStructure = "INVALID";

    creditCardNumber = get_long("Card number: ");

    // define how many digits the cardNumber has
    for (int i = 15; i >= 12; i--)
    {
        if (creditCardNumber / (long)pow(10, i) > 0)
        {
            quantityOfDigits = i;
            break;
        }
    }

    // Temporary integer to define card structure
    int cardStructureDefinition = (quantityOfDigits >= 12) ? creditCardNumber / (long)pow(10, quantityOfDigits - 1) : 0;

    if (cardStructureDefinition / 10 >= 1 && cardStructureDefinition / 10 <= 9)
    {
        switch (cardStructureDefinition)
        {
            case 34: case 37:
                cardStructure = "AMEX";
                break;
            case 51: case 52: case 53: case 54: case 55: case 22:
                cardStructure = "MASTERCARD";
                break;
            default:
                if (cardStructureDefinition / 10 == 4)
                {
                    cardStructure = "VISA";
                }
                break;
        }

        for (int i = quantityOfDigits; i >= 0; i--)
        {
            if (i % 2 == 0)
            {
                secondSum += creditCardNumber / (long)pow(10, i);
            }
            else
            {
                temp = creditCardNumber / (long)pow(10, i) * 2;
                firstSum += (temp >= 10) ? (temp / 10 + temp % 10) : temp;
            }

            creditCardNumber = creditCardNumber % (long)pow(10, i);
        }

        if ((firstSum + secondSum) % 10 != 0)
        {
            cardStructure = "INVALID";
        }
    }

    printf("%s\n", cardStructure);

    return 0;
}
