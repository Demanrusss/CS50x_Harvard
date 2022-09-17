// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

void freeFunction(node *);

// TODO: Choose number of buckets in hash table
const unsigned int N = 2051;
unsigned int quantityOfWords = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Get an index to choose right position in the hash-table
    short int index = hash(word);

    // Get the very first position in hash-table
    node *currentNode = table[index];

    // Look for the existence of the word in our linked list
    while (currentNode != NULL)
    {
        if (strcasecmp(currentNode->word, word) == 0)
        {
            return true;
        }
        else
        {
            currentNode = currentNode->next;
        }
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // Main idea is to get hash according to the length and first letter of a word
    return strlen(word) * 45 + toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open a file
    FILE *file = fopen(dictionary, "r");

    if (file == NULL)
    {
        printf("Could not open a file.\n");
        return false;
    }

    // Initialize an array in order to save characters of a word from dictionary
    char wordFromDict[LENGTH + 1];
    short int index;

    // Read a file word by word until the end of the file is reached
    while (fscanf(file, "%s", wordFromDict) != EOF)
    {
        node *newNode = malloc(sizeof(node));

        if (newNode == NULL)
        {
            printf("Could not enough memory.\n");
            return false;
        }

        strcpy(newNode->word, wordFromDict);
        index = hash(wordFromDict);

        if (table[index] != NULL)
        {
            newNode->next = table[index];
        }
        else
        {
            newNode->next = NULL;
        }

        table[index] = newNode;
        ++quantityOfWords;
    }

    fclose(file);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return quantityOfWords;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // For every element in hash-table
    for (int i = 0; i <= N; i++)
    {
        if (table[i] != NULL)
        {
            freeFunction(table[i]);
        }
    }

    return true;
}

// Recursively free node by node
void freeFunction(node *n)
{
    if (n->next == NULL)
    {
        free(n);
    }
    else
    {
        freeFunction(n->next);
    }
}