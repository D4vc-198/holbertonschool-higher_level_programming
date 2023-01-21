#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 99):
        if (n % 3) == 0:
            if n % 15 == 0:
                print("{}".format("FizzBuzz"), end=' ')
            else:
                print("{}".format("Fizz"), end=' ')
        elif (n % 5) == 0:
            if (n % 15) == 0:
                print("{}".format("FizzBuzz"), end=' ')
            else:
                print("{}".format("Buzz"), end=' ')
        elif n == 1:
            print("{}".format(n), end=' ')
        else:
            print("{}".format(n), end=' ')
