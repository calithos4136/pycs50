# i need it
from random import randrange


# the main stuff
def main():
    first, last = input("Enter your name, Maggot!").strip().title().split()

    hello(last)


# a function called hello, meant to identify maggots
def hello(last):
    print(f"{last}! You should be deployed to Sector {randrange(1, 89)}! GET GOING, MAGGOT-{last}!")
    return randrange(1, 89)


# calling the main function
main()
