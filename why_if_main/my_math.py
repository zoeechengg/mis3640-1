def square(x):
    return x * x

def main():
    n = int(input("enter:"))
    print("In my_math: square of {} is {}.".format(n, square(n)))

print('This is not in anyfunction.')

if __name__ == '__main__':
    main()
