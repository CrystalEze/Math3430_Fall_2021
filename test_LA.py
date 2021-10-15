import pytest
import LA

#test variables
vector_01 = [1, 2, 4]
vector_02 = [3, 1, 2]
vector_03 = [2, 4, 6]
vector_04 = [3, 6, 9]

scalar_01 = 5

matrix_01 = [[2, 8, 7],[4, 9, 1],[10, 4, 6]]
matrix_02 = [[2, 4, 6],[3, 6, 9],[4, 8, 12]]
matrix_03 = [[3, 4, 6],[8, 7, 2],[9, 12, 8]]

def test_add_vectors():
    #[1+3, 2+1, 4+2] = [4, 3, 6]
    assert LA.add_vectors(vector_01, vector_02) == [4, 3, 6]
    #[1+2, 2+4, 4+6] = [3, 6, 10]
    assert LA.add_vectors(vector_01, vector_03) == [3, 6, 10]

def test_scalar_vector_multi():
    #[5*1, 5*2, 5*4] = [5, 10, 20]
    assert LA.sca_vec_mult(vector_01, scalar_01) == [5, 10, 20]
    #[5*3, 5*1, 5*2] = [15, 5, 10]
    assert LA.sca_vec_mult(vector_02, scalar_01) == [15, 5, 10]

def test_scalar_matrix_multi():
    #[[5*2, 5*8, 5*7], [5*4, 5*9, 5*1], [5*10, 5*4, 5*6]] = [[10, 40, 35], [20, 45, 5], [50, 20, 20]]
    assert LA.sca_mat_mult(matrix_01, scalar_01) == [[10, 40, 35], [20, 45, 5], [50, 20, 30]]
    #[[5*3, 5*4, 5*6], [5*8, 5*7, 5*2], [5*9, 5*12, 5*8]] = [[15, 20, 30], [40, 35, 10], [45, 60, 40]]
    assert LA.sca_mat_mult(matrix_03, scalar_01) == [[15, 20, 30], [40, 35, 10], [45, 60, 40]]

def test_add_matrix():
    #[[2+2, 8+4, 7+6], [4+3, 9+6, 1+9], [10+4, 4+8, 6+12]] = [[4, 12, 13], [7, 15, 10], [14, 12, 18]]
    assert LA.add_matrix(matrix_01, matrix_02) == [[4, 12, 13], [7, 15, 10,], [14, 12, 18]]
    #[[2+3, 4+4, 6+6], [3+8, 6+7, 9+2], [4+9, 8+12, 12+8] = [[5, 8, 12], [11, 13, 11], [13, 20, 20]]
    assert LA.add_matrix(matrix_02, matrix_03) == [[5, 8, 12], [11, 13, 11], [13, 20, 20]]

def test_matrix_vector_multi():
    #[[1*2+4*2+4*10], [1*8+2*9+4*4], [7*1+2*1+4*6]] = [50, 42, 33]
    assert LA.mat_vec_mult(matrix_01, vector_01) == [50, 42, 33]
    #[[3*2+1*3+2*4], [3*4+1*6+2*8], [3*6+1*9+2*12]] = [17, 34, 51]
    assert LA.mat_vec_mult(matrix_02, vector_02) == [17, 34, 51]

def test_matrix_matrix_multi():
    assert LA.mat_mat_mult(matrix_01, matrix_02) == [[80, 76, 54], [120, 114, 81], [160, 152, 108]]
    assert LA.mat_mat_mult(matrix_02, matrix_03) == [[42, 84, 126], [45, 90, 135], [86, 172, 258]]