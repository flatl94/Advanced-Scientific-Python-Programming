import numpy as np
print('Exercise A: printing a null vector with a 1 as a fifth element.'+
      '\nNull was interpreted as empty, but there will be an exemple with zeros.')
# EXERCISES A
null_vect = np.empty((10))
null_vect[4] = 1
print('Exemple with empty: ',null_vect)
# EXERCISE A -VARIATION WITH ZEROS
zero_vect = np.zeros((10))
zero_vect[4] = 1
print('Exemple with zeros: ',zero_vect)
print('Exercise B: Creating a vector with a range between 10 and 49')
range_vect = np.arange(10,50)
print(range_vect)
print('Exercise C: Creating a reversed vector')
vect_a = np.array([1,2,3,4,5,16])
reve_a = vect_a[::-1]
print('The vector is: ',vect_a,';\nits reverse is: ', reve_a,'.')
print('Exercise D: Creating a 3 by 3 matrix with values between 0 and 8')
range_vect = np.arange(0,9)
range_mat = np.reshape(range_vect,(3,3))
print(range_mat)
print('Exercise E: Find the indices of zero elements in [1,2,0,0,4,0]')
array_test = np.array([1,2,0,0,4,0])
print(np.where(array_test == 0)[0])
print('Exercise F: Finding the mean of a random vector of size 30')
rand_vect = np.random.randint(0,100,size = 30)
print('The vector is: ',rand_vect, ' and the mean value is :',np.mean(rand_vect))
print('Exercise G: Creating a matrix with 1 in the borders and 0 in the inside')
mat_with_borders = np.zeros((10,10))
mat_with_borders[:,0] = 1
mat_with_borders[:,-1] = 1
mat_with_borders[0,:] = 1
mat_with_borders[-1,:] = 1
print(mat_with_borders)
print('Exercise H - I: Creating a chessboard')
chessboard_vect = np.zeros((8))
chessboard_vect[::2] = 1
rev_chessboard_vect = chessboard_vect[::-1]
chessboard_notile = np.array([chessboard_vect,rev_chessboard_vect,
                              chessboard_vect,rev_chessboard_vect,
                              chessboard_vect,rev_chessboard_vect,
                              chessboard_vect,rev_chessboard_vect],dtype=np.int32)

print('The chessboard is here. White to move: Nd3\n',chessboard_notile)
tile1 = np.tile([0,1],4)
tile2 = np.tile([1,0],4)
chessboard_tile = np.reshape(np.tile([tile1,tile2],4),(8,8))
print('Black answer with: e5\n',chessboard_tile)
print('Exercise J: Excluding elements')
z = np.arange(11)
new_z = z[np.logical_or(z<3, z>8)]
print(z, new_z)
print('Exercise K: Sort elements')
rand_vect = np.random.random(10)
sorted_vect = np.sort(rand_vect)
print(rand_vect, sorted_vect)
print('Exercise L: Comparing_matrices')
mat_a = np.random.randint(0,2,5)
mat_b = np.random.randint(0,2,5)
equal = np.equal(mat_a,mat_b)
print(mat_a, mat_b, equal)
print('Exercise M: squaring of matrix elements')
mat = np.arange(10, dtype=np.int32)
print('Original matrix: ',mat.dtype,mat)
mat *= mat
print('Squared matrix (without creating new instances): ',mat.dtype, mat)

print('Exercise N: Diagonal of a matrix')
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diag(C)
print(D)
