''' Lexicographic permutations
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the
digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?'''

digits = [0,1,2,3,4,5,6,7,8,9]

def swap(i, j):
    ''' swap values in digits at position i-1 and j-1 '''
    temp = digits[i]
    digits[i] = digits[j]
    digits[j] = temp

def nth_permutation(n):
    ''' permutes the global digits list n times assuming initially in lexicographic ordering '''
    N = len(digits)
    for _ in range(n-1): # offset count because original ordering is 1st permutation
        i = N-1
        while (digits[i-1] >= digits[i]):
            i = i-1
        j = N
        while(digits[j-1] <= digits[i-1]):
            j = j-1

        swap(i-1, j-1)

        i += 1
        j = N 
        while(i<j):
            swap(i-1,j-1)
            i += 1
            j -= 1

def main():
    nth_permutation(1000000)
    perm_str = ""
    for i in digits:
        perm_str += str(i)
    print perm_str

main()
