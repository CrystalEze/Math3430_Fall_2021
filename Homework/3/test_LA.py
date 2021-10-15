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

