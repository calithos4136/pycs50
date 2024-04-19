from git.source.sayings import hello


# a file to test the sayings.py file

# testing
def testHello():
    assert hello("David") == "Hello, David."
    assert hello() == "Hello, world."
