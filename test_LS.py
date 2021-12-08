import LS
import pytest


matrix_01 = [[5,6,2], [3,7,8], [2,6,3]]
matrix_02 = [[3,4,7], [2,9,6], [1,5,3]]
vector_01 = [0,1,0]
vector_02 = [1,4,2]

matrix_03 = [[5, 0, 0], [2, 1, 0], [1, 1, 3]]
vector_03 = [4, 1, 2]
matrix_04 = [[3, 0, 0], [5, 1, 0], [2, 3, 4]]
vector_04 = [5, 1, 2]

def test_back_substitution():
    assert LS.back_substitution(vector_03, matrix_03) == [0.5333333333333334, 0.33333333333333337, 0.6666666666666666]
    assert LS.back_substitution(vector_04, matrix_04) == [2.1666666666666665, -0.5, 0.5]

def test_least_squares():
    assert LS.Least_Squares(vector_01, matrix_01) == [-0.08235294117647059, -0.12941176470588237, 0.4]
    assert LS.Least_Squares(vector_02, matrix_02) == [0.5000000000000002, -4.4999999999999964, 8.499999999999993]