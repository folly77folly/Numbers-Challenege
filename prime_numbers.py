# 3. Write a Python function that takes a number as 
# a parameter and check the number is prime or not.
# Note : A prime number (or a prime) is a natural number 
# greater than 1 and that has no positive divisors other than 1 and itself

def solution(prime):

    #checking if all conditions match none prime numbers
    if prime <= 1:
        return f'{prime} not prime'     #not a prime 
    if prime == 2 or prime == 3 or prime == 5:
        return f'{prime} is prime'
    if prime % 2 == 0:                  #not a prime
        return f'{prime} not prime'    
    if prime % 3 == 0:                  #not a prime
        return f'{prime} not prime'    
    if prime % 5 == 0:                  # not a prime
        return f'{prime} not prime'     
    else:
        return f'{prime} is prime'



print(solution(269))