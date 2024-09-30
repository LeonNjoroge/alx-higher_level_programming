#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

#1. check last digit of number
#2. check if last digit is (LD>5) (LD==0)(LD<6 && LD != 0)


last_digit = abs(number) % 10

if last_digit == 0:
    print("Last digit of {} is {} and is 0\n".format(number,last_digit))
elif last_digit > 5:
    print("Last digit of {} is {} and is greater than 5\n".format(number,last_digit))
elif last_digit < 6 and last_digit != 0:
    print("Last digit of {} is {} and is less than 6 and not 0\n".format(number,last_digit))
