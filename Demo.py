import LA
import QR
import LS

print('Hello, my name is Crystal Eze and I am majoring in Mathematics. This is the library I have written.')
print('')

print('''My library consists of three different files called LA.py, QR.py, and LS.py which demonstrates
numerous linear equations. I will first start with the functions in LA.py, which contains 11 functions.''')
print('')

print('''The first function is add_vectors which takes two vectors and calculates their sum.''')
print('''Example, if vector_01 = [1,2,4] and vector_02 = [3,1,2], then add_vectors will return:''')
vector_01 = [1,2,4]
vector_02 = [3,1,2]
print(LA.add_vectors(vector_01, vector_02))
print('')

print('''The second function is sca_vec_mult which calculates the product of a scalar and a vector.''')
print('''Example, if vector_01 = [1,2,4] and scalar_01 = 5, then sca_vec_mult will return:''')
vector_01 = [1,2,4]
scalar_01 = 5
print(LA.sca_vec_mult(vector_01, scalar_01))
print('')

print('''The third function is sca_mat_mult which calculates the product of a scalar and a matrix.''')
print('''Example, if matrix_01 = [[2,8,7],[4,9,1],[10,4,6]] and scalar_01 = 5, then sca_mat_mult will return:''' )
matrix_01 = [[2,8,7],[4,9,1],[10,4,6]]
scalar_01 = 5
print(LA.sca_mat_mult(matrix_01, scalar_01))
print('')

print('''The fourth function is add_matrix which calculates the sums of two matrices.''')
print('''Example, if matrix_01 = [[2,8,7],[4,9,1],[10,4,6]] and matrix_02 = [[2,4,6],[3,6,9],[4,8,12]],
then add_matrix will return:''')
matrix_01 = [[2, 8, 7],[4, 9, 1],[10, 4, 6]]
matrix_02 = [[2, 4, 6],[3, 6, 9],[4, 8, 12]]
print(LA.add_matrix(matrix_01, matrix_02))
print('')

print('''The fifth function is mat_vec_mult which computes the product of a matrix and vector.''')
print('''Example, if matrix_02 = [[2,4,6],[3,6,9],[4,8,12]] and vector_02 = [3,1,2], then mat_vec_mult
will return:''')
matrix_02 = [[2, 4, 6],[3, 6, 9],[4, 8, 12]]
vector_02 = [3, 1, 2]
print(LA.mat_vec_mult(matrix_02, vector_02))
print('')

print('''The sixth function is mat_mat_mult which calculates the product of two matrices.''')
print('''Example, if matrix_01 =[[2,8,7],[4,9,1],[10,4,6]] and matrix_02 = [[2,4,6],[3,6,9],[4,8,12]],
then mat_mat_mult will return:''')
matrix_01 = [[2, 8, 7],[4, 9, 1],[10, 4, 6]]
matrix_02 = [[2, 4, 6],[3, 6, 9],[4, 8, 12]]
print(LA.mat_mat_mult(matrix_01, matrix_02))
print('')

print('''The seventh function is absolute which takes a scalar and returns its absolute value.''')
print('''Example, if test_scalar_a = -5j, then absolute will return:''')
test_scalar_a = -5j
print(LA.absolute(test_scalar_a))
print('')

print('''The eighth function is P_norm which takes a vector and calculates its p norm.''')
print('''Example, if test_vector_a = [3,4], then P_norm will return:''')
test_vector_a = [-3, 4]
print(LA.P_norm(test_vector_a))
print('')

print('''The ninth function is Infinity_norm which takes a vector and returns the infinity norm of that vector.''')
print('''Example, if test_vector_c = [7,6,1], then Infinity_norm will return:''')
test_vector_c = [7, 6, 1]
print(LA.Infinity_norm(test_vector_c))
print('')

print('''The tenth function is Input_Vector which takes  vector and computes either the p norm or the infinity
norm based off the boolean value given.''')
print('''Example, if test_vector_e = [5,-12], then Input_Vector will return:''')
test_vector_e = [5, -12]
print(LA.Input_Vector(test_vector_e, 2, True))
print('')

print('''The eleventh function is dot_product which takes two vectors and computes its inner product, or dot product.''')
print('''Example, if test_vector_g = [7,0,-2j] and test_vector_h = [1,-1j,4], then dot_product will return:''')
test_vector_g = [7, 0, -2j]
test_vector_h = [1, -1j, 4]
print(LA.dot_product(test_vector_g, test_vector_h))
print('')

print('''Next, I will do the functions in the QR.py, which contains 12 functions.''')
print('')

print('''The first function is Stable_GS which takes a matrix and computes its QR factorization.''')
print('''Example, if matrix_01 = [[1,0,5], [2,0,1]], then Stable_GS returns:''')
matrix_01 = [[1,0,5], [2,0,1]]
print(QR.Stable_GS(matrix_01))
print('')

print('''The second function is Orthonormal_Vectors which takes a matrix and orthonormalizes it.''')
print('''Example, if matrix_02 = [[1,0,1], [2,1,0]], then Orthonormal_Vectors will return:''')
matrix_02 = [[1,0,1], [2,1,0]]
print(QR.Orthonormal_Vectors(matrix_02))
print('')

print('''The third function is complex_con which takes a scalar and calculates its conjugate.''')
print('''Example, if test_scalar_02 = 5-8j, then complex_con will return:''')
test_scalar_02 = 5-8j
print(QR.complex_con(test_scalar_02))
print('')

print('''The fourth function is sign which takes a scalar and computes its sign.''')
print('''Example, if test_scalar_03 = -7, then sign will return:''')
test_scalar_03 = -7
print(QR.sign(test_scalar_03))
print('')

print('''The fifth function is calculate_V which takes a vector and computes its v builder.''')
print('''Example, if test_vector_02 = [1,2], then calculate_V will return:''')
test_vector_02 = [1, 2]
print(QR.calculate_V(test_vector_02))
print('')

print('''The sixth function is matrix_identity which takes a scalar and calculates its square identity matrix.''')
print('''Example, if test_scalar_04 = 1, then matrix_identity will return:''')
test_scalar_04 = 1
print(QR.matrix_identity(test_scalar_04))
print('')

print('''The seventh function is deep_copy which takes a matrix and calculates its deep copy.''')
print('''Example, if test_matrix_03 = [[5,2], [3,4]], then deep_copy will return:''')
test_matrix_03 = [[5, 2], [3, 4]]
print(QR.deep_copy(test_matrix_03))
print('')

print('''The eigth function is conjugate_transpose which takes a matrix and calculates its conjugate transpose.''')
print('''Example, if test_matrix_04 = [[5-8j,3], [4,7-3j]], then conjugate_transpose will return:''')
test_matrix_04 = [[5-8j, 3], [4, 7-3j]]
print(QR.conjugate_transpose(test_matrix_04))
print('')

print('''The ninth function is vec_vec_mult which takes two vectors and computes their product.''' )
print('''Example, if test_vector_03 = [3,6,2] and test_vector_04 = [5,8,7], then vec_vec_mult will return:''')
test_vector_03 = [3, 6, 2]
test_vector_04 = [5, 8, 7]
print(QR.vec_vec_mult(test_vector_03, test_vector_04))
print('')

print('''The tenth function is calculate_F which takes a vector and returns the F.''')
print('''Example, if test_vector_05 = [5.2,3.7], then calculate_F will return:''')
test_vector_05 = [5.2, 3.7]
print(QR.calculate_F(test_vector_05))
print('')

print('''The eleventh function is calculate_Q which takes a matrix and a scalar and returns the Q.''')
print('''Example, if test_matrix_05 = [[5.2,3.7], [5.2,3.7]] and test_scalar_05 = 1, then calculate_Q
will return:''')
test_matrix_05 = [[5.2,3.7], [5.2,3.7]]
test_scalar_05 = 1
print(QR.calculate_Q(test_matrix_05, test_scalar_05))
print('')

print('''The twelfth function is Householder_QR which takes takes a matrix and calculates its QR factorization.''')
print('''Example, if test_matrix_03 = [[2,2,1], [-2,1,2], [18,5,2]], then Householder_QR will return:''')
test_matrix_03 = [[2,2,1], [-2,1,2], [18,5,2]]
print(QR.Householder_QR(test_matrix_03))
print('')

print('''Finally, I will do the functions in LS.py, which contains only 2 functions.''')
print('')

print('''The first function is back_substitution which takes a matrix and a vector and computes its back
substitution.''')
print('''Example, if test_matrix_01 = [[5,6,2], [3,7,8], [2,6,3]] and test_vector_01 = [0,1,0], then
back_substitution will return:''')
test_matrix_01 = [[5, 0, 0], [2, 1, 0], [1, 1, 3]]
test_vector_01 = [4, 1, 2]
print(LS.back_substitution(test_vector_01, test_matrix_01))
print('')

print('''The second function is Least_Squares which takes a matrix and a vector and calculates its least squares
matrix.''')
print('''Example, iftest_matrix_01 = [[5,6,2], [3,7,8], [2,6,3]] and test_vector_01 = [0,1,0], then Least_Squares
will return:''')
test_matrix_01 = [[3, 0, 0], [5, 1, 0], [2, 3, 4]]
test_vector_01 = [5, 1, 2]
print(LS.Least_Squares(test_vector_01, test_matrix_01))