x = input("What is x? ")

if x.isdigit():
    x = float(x)
    print(f"x is {x}")
else:
    print("Only use numbers.")