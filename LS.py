import LA
import QR

def back_substitution(Vector: list, matrix_a: list[list[float]]) -> list:
    """Calculates the back substitution of a matrix and a vector

    First we inititialize result as our first solution, which is equal to the second negative index of our vector
    multiplied by the division of 1 over the second negative elements of the rows and colums of our matrix. Next,
    we create a for loop to go through the elements in the matrix and subtract 2, then subtract 1, and subtract
    1 again. We then create an inner for loop which gives us the value of our temporary float. We next append 
    that temporary float to our result before finally returning the result

    Args:
        Vector: A vector stored as a list
        matrix_a: A matrix stored as a list of lists
    
    Returns:
        The back substitution
    """

    length = len(matrix_a)-1
    result: list = [Vector[-1]*(1/(matrix_a[-1][-1]))]
    for current in range(length-1,-1,-1):
        temp = Vector[current]
        for i in range(len(result)):
            temp -= matrix_a[length-i][current]*result[i]
        temp *= 1/(matrix_a[current][current])
        result.append(temp)
    return result[::-1]

def Least_Squares(Vector: list, matrix_a: list[list[float]]) -> list:
    """Calculates the least squares solution of our input vector and matrix

    We start by setting our Q and R equal to our householder function of our matrix. We then take the
    conjugate transpose function of our Q and set it equal to what is named Q_sarcasm. We then use our matrix
    vector multiplication function and apply it to the parameters which is our Q_sarcasm and vector and
    set it equal to Q_awesomeness. We next use our previous back substitution function for our parameters R
    and Q_awesome and set that equal to back_hand. Finally, we return our back_hand which is equivalent to the
    least squares

    Args:
        Vector: A vector stored as a list
        matrix_a: A matrix stored as a list of lists

    Returns:
        The least squares solution of of our matrix and vector
    """

    [Q, R] = QR.Householder_QR(matrix_a)
    Q_sarcasm = QR.conjugate_transpose(Q)
    Q_awesomeness = LA.mat_vec_mult(Q_sarcasm, Vector)
    back_hand = back_substitution(Q_awesomeness, R)
    return back_hand

test_matrix_01 = [[5, 6, 2], [3, 7, 8], [2, 6, 3]]
test_vector_01 = [0, 1, 0]

result = Least_Squares(test_vector_01, test_matrix_01)
print(result)