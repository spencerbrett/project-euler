''' Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''

def digit_list(n):
    result = []
    while(n > 0):
        digit = n%10
        n = int(n/10)
        result.append(digit)
    return result

def is_palindrome(n):
    digits = digit_list(n)
    reverse = digits[:]
    reverse.reverse()
    if digits == reverse:
        return True
    return False

def main():
    largest_pal = 0
    for i in range(100,1000):
        for j in range(i, 1000):
            prod = i*j
            if(is_palindrome(prod) and prod > largest_pal):
                largest_pal = prod
    print largest_pal

main()
