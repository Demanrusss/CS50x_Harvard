#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Print the winner
    if (score1 == score2)
    {
        printf("Tie!\n");
    }
    else
    {
        if (score1 > score2)
        {
            printf("Player 1 wins!\n");
        }
        else
        {
            printf("Player 2 wins!\n");
        }
    }

    return 0;
}

int compute_score(string word)
{
    // Compute and return score for string
    int i = 0, score = 0;

    // Change every lowercase letter to uppercase
    while (word[i] != '\0')
    {
        word[i] = islower(word[i]) ? toupper(word[i]) : word[i];
        i++;
    }

    // Initialize to zero again just not to use another variable
    i = 0;

    // Enumerate every character
    while (word[i] != '\0')
    {
        // Use only uppercase letter to compute
        if (word[i] >= 65 && word[i] <= 90)
        {
            score += POINTS[(int)word[i] - 65];
        }

        i++;
    }

    return score;
}
