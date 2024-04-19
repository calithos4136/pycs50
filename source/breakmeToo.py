def main():
    num = getNum("What's a cool number?? ")
    print(f"A cool number is {num:.2f}.")


def getNum(prompt):
    while True:
        # trying, struggling
        try:
            x = float(input(prompt).strip())
        # oh, no! an error
        except ValueError:
            print("x must be a number!")
            # pass
        # yay! no error
        else:
            return x


main()
