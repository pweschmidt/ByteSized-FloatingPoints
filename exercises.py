from decimal import Decimal
import math
import sys
import numpy as np
from struct import pack, unpack

# First get some stats from the machine how
# Floating points and integers are represented

def getsys_info():
    print("**** Get Sys Info ***")
    # floating points
    print(sys.float_info)
    # integers
    print(sys.int_info)
    print("\n")

def print_float_as_bitstring():
    print("**** print bit strings ***")
    bin_integer = 2
    bin_floating_point = 2.0

    print("First, print integer value of 2 as bit string")
    print(f"{bin_integer:032b}")
 
    # for floating points a bit more work is needed
    print("Now print the value for 2 as floating point - 64 bit - which is default in Python")
    print_bitstring(bin_floating_point)

    # print the value for 0.1 as bitstring and Decimal and then 0.3
    print("Print the bitstring value for 0.1")
    print("3 different approaches are used")

    print("Print 0.1 as 64bit float")
    print_bitstring(0.1)

    print("print - using pack methods - as 32bit float")
    print_bitstring_differently(0.1)

    print("print as 32 bit float using numpy package")
    print_bitstring_numpy(0.1)

    print("Print the decimal value of 0.1")
    print(Decimal(0.1))

    print("Print the bitstring value for 0.3")
    print_bitstring(0.3)
    print("Print the decimal value of 0.3")    
    print(Decimal(0.3))

    print("Print the ")


    print("\n")
    
def print_bitstring(number):
    print("".join([f"{b:08b}" for b in pack(">d", number)]))

def print_bitstring_differently(number):
    bitstring = unpack('!I', pack('!f', number))[0]
    print(f"{bitstring:032b}")

def print_bitstring_numpy(number):
    bitstring = np.binary_repr(np.float32(number).view(np.int32), width=32)
    print(bitstring)



## exercise 3, what is 0.1 + 0.2?
def basic_arithmetic():
    print("*** Basic Arithmetics ***")
    # should expect Tru
    print(0.1 + 0.2 == 0.3)
    # what does the sum actually look like
    print(Decimal(0.1 + 0.2))

    print(math.isclose(0.1 + 0.2, 0.3))
    print("\n")

## exercise 4 catastrophic cancellations
def catastrophic_cancellations():
    print("*** Catastrophic Cancellations ***")
    a = math.pi
    b = 6.022e23

    a = (b + a) - b
    print(a)
    print("\n")

def associative_laws():
    print("*** Associative Laws ***")
    a = 6.022e23
    # both should be the same
    print( a - a + 1)
    print( 1 + a - a)
    print("\n")

## exercise 5 accumulative errors
def accumulations():
    print("*** Rounding Errors Accumulation ***")
    total = 0.0
    for _ in range(10):
        total += 0.1
    print(total == 1.0)   # False
    print(total)          # 0.9999999999999999

    #better is to use a math function
    print(math.fsum([0.1] * 10) == 1.0)
    print("\n")


# get info first

# getsys_info()

# try to print numbers as a bit string

print_float_as_bitstring()

# basic_arithmetic exercise

# basic_arithmetic()

# catastrophic cancellation

# catastrophic_cancellations()

# do associative laws still hold?

# associative_laws()

# how errors can accumulate

# accumulations()


