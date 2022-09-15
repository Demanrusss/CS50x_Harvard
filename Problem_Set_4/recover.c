#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#define BLOCK_SIZE 512

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check for number of arguments inserted from command line
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    char *file = argv[1];

    // Open the file for reading
    FILE *filePtr = fopen(file, "r");

    // Check if the file opened correctly
    if (filePtr == NULL)
    {
        printf("File %s cannot be opened.\n", file);
        return 1;
    }

    // Initialize necessary variables for buffer, name of new file and counter
    BYTE buffer[BLOCK_SIZE];
    char newFilename[9];
    FILE *newFilePtr;
    int counter = 0;

    // Read source file by block till the end
    while (fread(&buffer, BLOCK_SIZE, 1, filePtr) == 1)
    {
        // Check for JPEG Format
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff)
        {
            if (buffer[3] >= 0xe0 && buffer[3] <= 0xef)
            {
                if (counter != 0)
                {
                    // Close the new file
                    fclose(newFilePtr);
                }

                // Create name of a new file
                sprintf(newFilename, "%d%d%d.jpg", counter / 100, counter % 100 / 10, counter % 100 % 10);

                // Create a new file
                newFilePtr = fopen(newFilename, "w");

                // Check if the file created correctly
                if (newFilePtr == NULL)
                {
                    printf("File %s cannot be created.\n", newFilename);
                    return 1;
                }

                // Fill in the new file with bytes from buffer
                fwrite(buffer, BLOCK_SIZE, 1, newFilePtr);
                ++counter;
            }
        }
        else if (counter != 0)
        {
            fwrite(buffer, BLOCK_SIZE, 1, newFilePtr);
        }
    }

    // Close the last file
    fclose(newFilePtr);

    // Close source file
    fclose(filePtr);

    return 0;
}