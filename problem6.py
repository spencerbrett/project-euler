''' Sum square difference
The sum of the squares of the first 10 natural numbers is,

1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2 + 7^2 + 8^2 + 9^2 + 10^2 = 385

The square of the sum of the first 10 natural numbers is,

(1 + 2 + ... + 10)^2

Hence the difference between the sum of the squares of the first 10 natural numbers is
3025-385 = 2640

Find the difference between the sum of the squares of the first 100 natural numbers
and the square of the sum '''

def sumSquares(nums):
    total = 0
    for i in nums:
        total += i**2
    return total

def squareSum(nums):
    return sum(nums)**2

def main():
    n = range(1,101)
    print abs(squareSum(n) - sumSquares(n))

main()
