''' Largest Prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143? '''

import math

def is_prime(n):
    nrt = int(math.sqrt(n))
    for i in range(2,nrt+1):
        if(n%i == 0):
            return False
    return True

def prime_factors(n):
    result = [1]
    nrt = int(math.sqrt(n))
    for i in range(2,nrt+1):
        if(n%i==0 and is_prime(i)):
            result.append(i)
            if(is_prime(int(n/i))):
                result.append(i)
    return result

def main():
    print max(prime_factors(600851475143))

main()
