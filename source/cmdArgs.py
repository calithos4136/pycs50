import sys

try:
    print("Hello, my name is", sys.argv[1].title())
except IndexError:
    print("Specify your name in the parameters when executing.")
