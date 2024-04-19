def main():
    # getting variables
    x = int(input("Enter height."))
    y = int(input("Enter width."))

    # printing the block
    printBlock(x, y)


def printBlock(height, width):
    #  for each row
    for _ in range(height):
        # printing the amt of cubes in each row
        print("#" * width)


# ez loop
while True:
    main()
