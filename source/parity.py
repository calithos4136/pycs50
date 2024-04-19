# main stuff
def main():
    # defining a number by user input
    x = int(input("Enter a number:").strip())

    # even or odd
    if isEven(x):
        print("Even")

    else:
        print("Odd")


def isEven(n):
    # even or odd
    return n % 2 == 0


main()
