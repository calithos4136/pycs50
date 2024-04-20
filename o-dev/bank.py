
# AUTHOR: CALITHOS4136

# get user input
text = input("Greeting: ").strip().lower()

# set the compensation price
compensation = 0

# testing the text

if text.find("hello"):

    # if there is a sudo greeting
    if not text.find("h"):
        compensation = 20

    # if there is no greeting at all
    else:
        compensation = 100


print(f"${compensation}")
# EOF
