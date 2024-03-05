#!/usr/bin/python

from math import ceil,sqrt
@profile
def gen_primes(n):
    l = range(2,n)
    primes = []
    for j in range(0,len(l)):
        p = True 
        for d in primes: #
            if(d > sqrt(l[j])): # 34% 700 micros
                break
            if(l[j] % d == 0): # 25% 500 micros
                p = False 
                break;
        if(p):
            primes.append(l[j])
    print(len(primes))
    return primes

@profile
def factorize(n,primes):
    factors = []
    init_n = n
    for p in primes:
        while(n%p == 0): # 34% 22000 micros
            n = n/p
            factors.append(p)
        if(p > sqrt(n)): # 28% 17000 micros
            break
    if(n > 1):
        factors.append(n)
    return factors
"""
optimization must be performed on the factorize function. While other functions 
could in principle be speed up, factorize is the function which runs for most of 
the time for the whole script. Some operations must occur in here. In particular,
most of the time is used to check if residuals from the divisions are zero and if
the prime number is a square root of the problem.

"""    
def phi(n,primes):
    factors = factorize(n,primes) # 88% of the time is occupied by this operation.
    p = 1

    for i in range(2,n):
        flag = True
        for f in factors:
            if i%f == 0:
                flag = False
                break
        if flag:
            p+=1
    return p

@profile
def fast_phi(n,primes):
    factors = factorize(n,primes)
    phi = factors[0]-1
    for i in range(1,len(factors)):
        if(factors[i] == factors[i-1]):
            phi *= (factors[i]-1)*(factors[i])/(factors[i]-1)
        else:
            phi *= (factors[i]-1)
    return phi

primes = gen_primes(1000)
m = 10000
#m = 8
fraq = 0
for i in range(2,m+1):
    fraq += fast_phi(i,primes)

print(fraq)
