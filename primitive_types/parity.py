'''
Write expressions that use bitwise operators, equality checks, and Boolean operators to do the following
in O(1) time
1. Right propagate the rightmost set bit in x, e.g., turns (01010000)_2 to (01011111)_2
2. Compute x mod a power of two, e.g., returns 13 for 77 mod 64
3. Test if x is a power of 2, i.e., evaluates to true for x = 1, 2, 4, 8..., false for all other values.
'''

def q1(x):
    return x | (x-1)

def q2(x, m):
    return x & (m-1)

def q3(x):
    if (x & (x-1) == 0):
        return True
    else:
        return False
