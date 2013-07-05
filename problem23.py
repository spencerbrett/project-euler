''' Non-abundant sums
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that
28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called
abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be
written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all 
integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper 
limit cannot be reduced any further by analysis even though it is known that the greatest number that 
cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant 
numbers.'''

import math

def prop_divisors(n):
    ''' Returns a list of the proper divisors of integer n '''
    divs = [1]
    n_rt = int(math.sqrt(n)) # The minimum limit for factor checking
    for i in xrange(2,n_rt+1):
        if n%i == 0: # check if it divides evenly
            divs.append(i)
            divs.append(int(n/i)) # add the factor pair 
    divs.sort()
    if n_rt*n_rt == n: divs.remove(n_rt) # remove the duplicate for the case of perfect squares
    return divs

def abundant_nums(UPPER_LIM = 28123):
    ''' Returns a unique set of abundant numbers '''
    ab_nums = []
    for n in xrange(12,UPPER_LIM+1):
        if sum(prop_divisors(n)) > n:
            ab_nums.append(n)
    ab_nums.sort()
    return set(ab_nums)
    
def sum_combination(nums):
    ''' Returns a unique set of all possible sums between 2 numbers in the argument set '''
    c = len(nums) # cardinality of nums set
    n = list(nums)
    result = set()
    for i in range(c):
        for j in range(i,c):
            result.add(n[i]+n[j])
    return result

def main(UPPER_LIM = 28123):
    # sum of the set difference between positive integers and numbers that are the sum of two abundant numbers
    # This is equal to all the positive integers which cannot be written as the sum of two abundant numbers
    print sum(set(range(1,UPPER_LIM+1)) - sum_combination(abundant_nums()))

main()
