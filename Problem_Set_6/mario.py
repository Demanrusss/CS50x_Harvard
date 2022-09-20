# Use library provided cs50
from cs50 import get_int

# Ask until user inputs right integer
while True:
    integer = get_int("Height: ")
    if 0 < integer < 9:
        break
# Draw the picture
for i in range(integer):
    j = integer
    while j > i + 1:
        print(" ", end="")
        j -= 1
    j = 1
    while j <= i + 1:
        print("#", end="")
        j += 1
    print("  ", end="")
    j = 1
    while j <= i + 1:
        print("#", end="")
        j += 1
    print()