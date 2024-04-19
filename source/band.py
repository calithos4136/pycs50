import csv

# using csv to read and write data
members = []

with open("persis/names.csv") as file:
    """    
    for line in file:
        name, instrument, drug = line.rstrip().split(",")
        member = {"name": name, "instrument": instrument, "drug": drug}
        members.append(member)
    """
    reader = csv.DictReader(file)
    for row in reader:
        member = {"name": row["name"], "instrument": row["instrument"], "drug": row["drug"]}
        members.append(member)

# lambda accesses an anonymous function so we dont have to write a new one
for member in sorted(members, key=lambda key: member["name"]):
    print(f"{member['name']} plays {member['instrument']} and is always using {member['drug']}")
