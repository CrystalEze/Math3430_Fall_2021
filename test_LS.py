import LS
import pytest


matrix_01 = [[5,6,2], [3,7,8], [2,6,3]]
matrix_02 = [[3,4,7], [2,9,6], [1,5,3]]
vector_01 = [0,1,0]
vector_02 = [1,4,2]


def test_least_squares():
    assert LS.Least_Squares(matrix_01, vector_01) == [-0.0823529411764704,-0.12941176470588234,0.39999999999999947]
    assert LS.Least_Squares(matrix_02, vector_02) == [0.49999999999943157,-4.499999999994543,8.499999999989086]