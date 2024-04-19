def main():
    x = int(input("What is x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

#making sure main is only called when file is directly run
if __name__ == "__main__":
    main()
