from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
ranksum = np.zeros((1))

if rank != 0:
    data = rank+1
elif rank == 0:
    data = 0
data = comm.gather(data, root=0)

if rank == 0:
    print(sum(data))