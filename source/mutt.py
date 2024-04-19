# the main stuff
def main():
    num = fetchNum()
    bark(num)


# getting the numbers from the MAGGOT
def fetchNum():
    while True:
        n = int(input("HOW MANY TIMES DID MY PRECIOUS KURBROW BARK?"))
        if n > 0:
            print("DID IT SOUND LIKE THIS, MAGGOT?")
            return n
        elif n == 0:
            print("DO YOU REALLY THINK I DIDN'T HEAR HIM BARK! YOU MAGGOT! DON'T LIE TO ME!\n SO, ", end="")


# emulating the barking
def bark(n):
    for _ in range(n):
        print("BARK")


main()
