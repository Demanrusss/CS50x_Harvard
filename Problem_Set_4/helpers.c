#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int gray;

    for (int i = 0; i < height; i++) // rows
    {
        for (int j = 0; j < width; j++) // columns
        {
            // Calculate average grade of gray
            gray = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);

            // Change colour to gray grade calculated above
            image[i][j].rgbtBlue = image[i][j].rgbtGreen = image[i][j].rgbtRed = gray;
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++) // rows
    {
        for (int j = 0; j < width / 2; j++) // columns
        {
            // temporary integer especially "char" type is pretty enough for number 255
            char temp[3];

            // Save values of each colour from the left side
            temp[0] = image[i][j].rgbtBlue;
            temp[1] = image[i][j].rgbtGreen;
            temp[2] = image[i][j].rgbtRed;

            // Copy values of each colour from the right side to the left
            image[i][j].rgbtBlue = image[i][width - (j + 1)].rgbtBlue;
            image[i][j].rgbtGreen = image[i][width - (j + 1)].rgbtGreen;
            image[i][j].rgbtRed = image[i][width - (j + 1)].rgbtRed;

            // Copy values of each colour from temp to the right
            image[i][width - (j + 1)].rgbtBlue = temp[0];
            image[i][width - (j + 1)].rgbtGreen = temp[1];
            image[i][width - (j + 1)].rgbtRed = temp[2];
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Initialize a copy of an image
    RGBTRIPLE copy[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }


    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Initialize additional integers of colour to sum them up
            int sumOfBlueValues = 0;
            int sumOfGreenValues = 0;
            int sumOfRedValues = 0;

            int counter = 0;

            // Get colours in every pixel in a box 3x3 of the pixel chosen above (i,j)
            for (int x = i - 1; x <= i + 1; x++)
            {
                // Check if it is not out of the image
                if (x >= 0 && x < height)
                {
                    for (int y = j - 1; y <= j + 1; y++)
                    {
                        // Check if it is not out of the image
                        if (y >= 0 && y < width)
                        {
                            //Sum up colour values
                            sumOfBlueValues += copy[x][y].rgbtBlue;
                            sumOfGreenValues += copy[x][y].rgbtGreen;
                            sumOfRedValues += copy[x][y].rgbtRed;

                            ++counter;
                        }
                    }
                }
            }

            image[i][j].rgbtBlue = round((float)sumOfBlueValues / counter);
            image[i][j].rgbtGreen = round((float)sumOfGreenValues / counter);
            image[i][j].rgbtRed = round((float)sumOfRedValues / counter);
        }
    }

    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // Initialize two Sobel arrays
    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Initialize additional integers to sum up values of colour
            double GxBlue = 0, GxGreen = 0, GxRed = 0;
            double GyBlue = 0, GyGreen = 0, GyRed = 0;

            for (int x = 0; x <= 2; x++)
            {
                // Check if it is not out of the image
                if (i + x - 1 >= 0 && i + x - 1 < height)
                {
                    for (int y = 0; y <= 2; y++)
                    {
                        // Check if it is not out of the image
                        if (j + y - 1 >= 0 && j + y - 1 < width)
                        {
                            GxBlue += copy[i + x - 1][j + y - 1].rgbtBlue * Gx[x][y];
                            GxGreen += copy[i + x - 1][j + y - 1].rgbtGreen * Gx[x][y];
                            GxRed += copy[i + x - 1][j + y - 1].rgbtRed * Gx[x][y];
                            GyBlue += copy[i + x - 1][j + y - 1].rgbtBlue * Gy[x][y];
                            GyGreen += copy[i + x - 1][j + y - 1].rgbtGreen * Gy[x][y];
                            GyRed += copy[i + x - 1][j + y - 1].rgbtRed * Gy[x][y];
                        }
                    }
                }
            }

            // Initialize values for colours
            int blue, green, red;

            // Get Sobel operator
            blue = round(sqrt(GxBlue * GxBlue + GyBlue * GyBlue));
            green = round(sqrt(GxGreen * GxGreen + GyGreen * GyGreen));
            red = round(sqrt(GxRed * GxRed + GyRed * GyRed));

            // Write down new values to current pixel
            image[i][j].rgbtBlue = (blue > 255) ? 255 : blue;
            image[i][j].rgbtGreen = (green > 255) ? 255 : green;
            image[i][j].rgbtRed = (red > 255) ? 255 : red;
        }
    }

    return;
}
