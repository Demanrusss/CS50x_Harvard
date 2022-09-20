#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main(void)
{
    // Initialize necessary variables
    string text = get_string("Text: ");
    int letters = 0;
    int words = 1;
    int sentences = 0;

    // Count quantity of letterss, words, sentences
    for (int i = 0; i < strlen(text); i++)
    {
        // Check for letters
        if (isalpha(text[i]))
        {
            ++letters;
        }

        // Check for words
        if (text[i] == ' ')
        {
            ++words;
        }

        // Check for sentences
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            ++sentences;
        }
    }

    // Calculate Coleman-Liau Index
    float CLI = 0.0588 * ((float)letters / words * 100) - 0.296 * ((float)sentences / words * 100) - 15.8;

    // Define grade
    if (CLI < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (round(CLI) >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %0.f\n", round(CLI));
    }

    return 0;
}