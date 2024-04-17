#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i >= 1:
        print(f'{i}')
        i -= 1
    print("Happy New Year!")
        

def square_integers(int_list):
    int_list = [int * int for int in int_list]
    return int_list

def fizzbuzz():
    i = 1
    for i in range(1,101):
        if(i % 5 == 0 and i % 3 == 0):
            print("FizzBuzz")
        elif(i % 3 == 0):
            print("Fizz")
        elif(i % 5 == 0):
            print("Buzz")
        else: print(f'{i}')
