#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[])
{
    // Initialization of array
    int alphabet[2][26] = {{'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'},
                           {0}};
    // Initialization of variables in order to check input cipher
    int letters = 0, otherSymbols = 0;

    // Check if the input consists of only 2 arguments
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // Convert the input and Fill in the array with cipher
    if (strlen(argv[1]) == 26)
    {
        // Convert second argument to Uppercase
        for (int i = 0; i <= 26 - 1; i++)
        {
            argv[1][i] = toupper(argv[1][i]);
        }

        // Fill in the array of cipher
        for (int i = 0; i <= 26 - 1; i++)
        {
            alphabet[1][i] = argv[1][i];

            // Check if only one letter was used
            if (strchr(argv[1], alphabet[0][i]) == NULL)
            {
                printf("Key must contain each letter exactly once.\n");
                return 1;
            }
        }
    }
    else
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    // Get plaintext and create array of symbols for ciphertext
    string plaintext = get_string("plaintext:  ");
    char ciphertext[100] = {0};

    // Enumerate every symbol from plaintext
    for (int i = 0; plaintext[i] != '\0'; i++)
    {
        // Check if the symbol is a letter of uppercase according to our array
        if (toupper(plaintext[i]) >= 65 && toupper(plaintext[i]) <= 90)
        {
            char letter = alphabet[1][(int)toupper(plaintext[i]) - 65];
            ciphertext[i] = (isupper(plaintext[i])) ? letter : tolower(letter);
        }
        else
        {
            ciphertext[i] = plaintext[i];
        }
    }

    // Print out the ciphertext
    printf("ciphertext: %s\n", ciphertext);

    return 0;
}
