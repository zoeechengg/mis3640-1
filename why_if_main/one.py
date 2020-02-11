def func():
    print("func() in one.py")


def main():
    print("Main function in one.py")


if __name__ == "__main__":
    print(__name__)
    main()
    print("one.py is being run directly")
else:
    print(__name__)
    print("one.py is being imported into another module")
