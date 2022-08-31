#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height, i, j, k;

    do
    {
        height = get_int("Height: ");
    } while (height < 1 || height > 8);

    for (i = 1; i <= height; i++)
    {
        for (j = height; j > i; j--)
            printf(" ");

        for (k = 1; k <= i; k++)
            printf("#");

        printf("  ");

        for (k = 1; k <= i; k++)
            printf("#");

        printf("\n");
    }
}
