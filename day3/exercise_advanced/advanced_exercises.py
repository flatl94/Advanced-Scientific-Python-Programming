print('Advanced exercises with numpy.')
print('Exercise A: normalize coordinates')
import numpy as np
coord_mat = np.array( [[1.0, 2.0, 10], [3.0, 4.0, 20], [5.0, 6.0, 30], [7.0, 8.0, 40]])
norm_mat = np.divide(coord_mat,np.reshape(np.max(coord_mat,1),(4,1)))
print(norm_mat)
print('Exercise B: Generate the diagonal using fancy indexing.')
general_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
list_indices = [3*i for i in range(3)]
dial_vector = general_array.reshape(np.size(general_array))[list_indices]
print(general_array,'\n', dial_vector)
print('Exercise C: Create a matrix 10x3 and extract the closest number to 0.75')
mat_rand = np.random.random(size =30).reshape((10,3))
print(mat_rand)
mat_dist = np.abs(mat_rand - 0.75)
mat_closest = np.zeros((10,3))
for i in range(10):
    mat_closest[i,:] = np.where(mat_dist[i,:] == np.min(mat_dist[i,:]),1,0)
print(mat_closest)
print('Exercise D: shape of fancy indexing.')
x = np.empty((10, 8, 6))

idx0 = np.zeros((3, 8)).astype(int)
idx1 = np.zeros((3, 1)).astype(int)
idx2 = np.zeros((1, 1)).astype(int)

x[idx0, idx1, idx2]
print(np.shape(x),'\n',
    np.shape(x[idx0]),'\n',
    np.shape(x[idx1]),'\n',
    np.shape(x[idx2]),'\n',
    np.shape(x[idx0,idx1]),'\n',
    np.shape(x[idx0,idx2]),'\n',
    np.shape(x[idx1,idx2]),'\n',
    np.shape(x[idx0,idx1,idx2]))
print('Exercise E: Stides.')
x = np.arange(12, dtype=np.int32).reshape((3, 4))
print(x)
z = np.lib.stride_tricks.as_strided(x, shape=(2, 3, 2, 2),
                                    strides=(16,4,16,4))
print(z)





