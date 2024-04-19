names = []


def main():
    readNames()


def writeNames():
    name = input("What is your name? ").title()

    with open("persis/names.txt", "a") as file:
        file.write(name + "\n")
        # file.close()


def readNames():
    with open("persis/names.txt", "r") as file:
        for line in file:
            names.append(line.rstrip())
    for name in sorted(names, reverse=True):
        print(f"Hello, {name}.")


if __name__ == "__main__":
    main()
