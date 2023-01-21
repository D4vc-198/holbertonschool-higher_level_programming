#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 100):
        if n % 3 == 0:
            if n % 15 == 0:
                print(" FizzBuzz")
            else:
                print(" Fizz")
        elif n % 5 == 0:
            if n % 15 == 0:
                print(" FizzBuzz")
            else:
                print(" Buzz")
        elif n == 1:
            print("{}".format(n), end='')
        else:
            print("{}".format(n), end='')
