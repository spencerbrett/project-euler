''' Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10
without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

This is essentially the LCM of the set of digits from 1 to 20. There are many
common factors however, so we can eliminate many. The resultant set is:
{20, 19, 18, 17, 16, 15, 14, 13, 12, 11}'''

def gcd(a,b):
    '''Return greatest common divisor using Euclid's Algorithm.'''
    while b:
        a, b = b, a % b
    return a

def lcm(a,b):
    '''Return least common multiple.'''
    return a * b // gcd(a, b)

def main():
    print reduce(lcm, range(11,21)) # reduce is an implementation of currying

main()
