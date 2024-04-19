import csv

name = input("What is your name? ").title()
instrument = input("What do you play? ").title()

# opening a file
with open("persis/members.csv", "a") as file:
    # field names ensures the writer understands order
    writer = csv.DictWriter(file, fieldnames=["name", "instrument"])
    writer.writerow({"name": name, "instrument": instrument})