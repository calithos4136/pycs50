
#AUTHOR: CALITHOS4136

#get user input
text = input("Expression: ").strip()

x = text.split(" ")[0]
y = text.split(" ")[1]
z = text.split(" ")[2]

if y.__eq__("+"):
    print(float(x) + float(z))
elif y.__eq__("-"):
    print(float(x) - float(z))
elif y.__eq__("/"):
    print(float(x) / float(z))
elif y.__eq__("*"):
    print(float(x) * float(z))


#EOF
