'''
Solve the folowing problem in 0(1) time and space.
1. Write a program which takes as input a nonnegative integer x and returns a number y
   which is not equal to x, but has the same weight as x and
   their difference |x-y|, is as small as possible.
'''

def q1(x):
    y = x ^ (x >> 1)
    z = y & ~(y-1)
    x ^= z | z << 1
    return x
