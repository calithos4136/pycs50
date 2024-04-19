# loop parameters so the question cannot be bypassed
run = 1
while 0 != run:

    # start the inquisition
    answer = input("Do you like bugs?")

    # responding to user
    if answer.strip().lower().__eq__("yes"):

        # FOOLISH ANSWER
        print("NOOOOO, YOU CAN'T LIKE BUGS! TAKE THEM TO THE DETENTION CENTER!")
        run = 0

    elif answer.strip().lower().__eq__("no"):

        # AHHHHH BUGS ARE SCARY
        print("GOOD! Now, don't allow any bugs to enter the mainframe!, GO, CHILD! STOP THEM!")
        run = 0

    else:

        print("You fool, don't dodge my question!")

print()
# EOF
