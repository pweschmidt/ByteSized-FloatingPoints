from decimal import Decimal
import math
import sys
import numpy as np

# First get some stats from the machine how
# Floating points and integers are represented

def getsys_info():
    # floating points
    print(sys.float_info)
    # integers
    print(sys.int_info)

## exercise 3, what is 0.1 + 0.2?
def basic_arithmetic():
    # should expect Tru
    print(0.1 + 0.2 == 0.3)
    # what does the sum actually look like
    print(Decimal(0.1 + 0.2))

    print(math.isclose(0.1 + 0.2, 0.3))

## exercise 4 catastrophic cancellations
def catastrophic_cancellations():
    a = math.pi
    b = 6.022e23

    a = (b + a) - b
    print(a)

def associative_laws():
    a = 6.022e23
    # both should be the same
    print( a - a + 1)
    print( 1 + a - a)

## exercise 5 accumulative errors
def accumulations():
    total = 0.0
    for _ in range(10):
        total += 0.1
    print(total == 1.0)   # False
    print(total)          # 0.9999999999999999

    #better is to use a math function
    print(math.fsum([0.1] * 10) == 1.0)


