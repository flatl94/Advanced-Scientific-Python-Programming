# Program to multiply two matrices using nested loops

# let's say I don't want to use numpy.

# The script has been transformed into a function and then was run.

import random
import time

@profile
def test_fun():
    N = 250

    # NxN matrix
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])

    # Nx(N+1) matrix
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])

    # result is Nx(N+1)

    result1 = []
    for i in range(N):
        result1.append([0] * (N+1))
    start_time1 = time.time()
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)): # < --- THIS OPERATION ALONE TAKES MORE THAN 23% OF THE COMULATIVE RUNNING TIME
                result1[i][j] += X[i][k] * Y[k][j] # < --- THIS OPERATION ALONE TAKES MORE THAN 70% OF THE COMULTAIVE RUNNING TIME
    end_time1 = time.time()
    print('original solution: ',end_time1-start_time1)
    
    result2 = []
    for i in range(N):
        result2.append([0] * (N+1))
    start_time2 = time.time()
    # iterate through rows of X
    for i in range(N):
        # iterate through columns of Y
        for j in range(N+1):
            # iterate through rows of Y
            result2[i][j] = sum([X[i][k]*Y[k][j] for k in range(N)])
    end_time2 = time.time()
    print('new solution: ',end_time2-start_time2)
    if result1 == result2:
        print('And the "matrices" are also equal...')
"""
Minor loop rearrangements could in principle reduce the number of calculations, in
particular by performing more operations at once. However, this operation could reduce
the running time only by a small amount of time. Using numpy these operations are much faster.

"""

@profile
def optimized_fun():
    import numpy as np
    N = 250

    # NxN matrix
    X = np.random.randint(100, size=(N,N))
    Y = np.random.randint(100, size=(N,N+1))
    
    result = X @ Y

    # result is Nx(N+1)

test_fun()
optimized_fun()