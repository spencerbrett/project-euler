''' Reciprocal cycles
A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1/2  = 0.5
1/3  = 0.(3)
1/4  = 0.25
1/5  = 0.2
1/6  = 0.1(6)
1/7  = 0.(142857)
1/8  = 0.125
1/9  = 0.(1)
1/10 = 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.'''

def decSequenceLength():
    seqLen = 0
    n = 0
    for i in range(1000,0,-1): # count down because the max seq len is d-1 for 1/d because of remainders
        if seqLen >= i: # seqLen couldn't get any bigger because numbers are getting smaller
            return n

        remainders = [0]*i # initialize a list of size i to zero
        value = 1
        pos = 0

        while (remainders[value] == 0 and value != 0):
            remainders[value] = pos
            value *= 10
            value %= i
            pos += 1

        if (pos - remainders[value] > seqLen):
            seqLen = pos - remainders[value]
            n = i
    return i

print decSequenceLength()
