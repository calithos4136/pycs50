import sys
# using command parameters. in this ex, a name, or set of names
# error handling
if len(sys.argv) < 2:
    sys.exit("Too few args!")

for arg in sys.argv[1:]:

    print("Hello, my name is", arg.title())
