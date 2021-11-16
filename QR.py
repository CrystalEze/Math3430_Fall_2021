import LA

#1

def Stable_GS(matrix_a: list[list[float]]) -> list[list[float]]:
    """Implements the stable version of a Gram-Schmidt reduced QR factorization

    First we start by setting our three variables. Q is an empty list, V is also an empty list,
    R is a matrix filled with zeros and is the same size as matrix A, and the v is also a float 
    equivalent to 0. After we initialize the variables, we create our first for loop to run each element in
    matrix A and append the elements to our V input. For each column in our vector, the corresponding columns 
    of our R are set equal to our LA p-norm function with the vriable V[column] and will be be appended to our Q 
    which is the LA scalar vector multiplication function with the variables V[column] and 1 divided by the diagonal 
    inputs of R. Inside the same for loop, we will create another for loop that goes through the rows, starting
    from our column + 1 all the way through the length of our Matrix A. It then overrides our R column and rows 
    with the LA dot product function with variables Q and V which represents the corresponding column and row. 
    Next we will override the v with our LA scalar vector multiplication function with the variables
    Q and -R, Q representing our row and -R representing both column and row, or the diagonal inputs of R.
    Finally our V of the rows is set to the LA function for adding vectors with the variables V[column] and the 
    float v before returning the result of Q and R.

    Args:
        matrix_a: A matrix which is the result of our Q and R, stored as a list of lists
    
    Returns:
        A list of two matrices, the first being Q, and the second being R. Q being the orthogonal matrix and
        R being the triangular matrix
    """

    Q: list[complex or float] = []
    V: list[complex or float] = []
    R: list[complex or float] = [[0,0,0], [0,0,0]]
    v = 0

    for element in matrix_a:
        V.append(element)
    for column in range(len(matrix_a)):
        R[column][column] = LA.P_norm(V[column])
        Q.append(LA.sca_vec_mult((V[column]), (1/R[column][column])))
        for rows in range(column + 1, len(matrix_a)):
            R[column][rows] = LA.dot_product(Q[column], V[rows])
            v = LA.sca_vec_mult(Q[column], -R[column][rows])
            V[rows] = LA.add_vectors(V[rows], v)
    return [Q,R]


#2

def Orthonormal_Vectors(matrix_a: list[list[float]]) -> list[list[float]]:
    """Creates a list of orthonormal vectors

    First take each column in your matrix and set it equal to any variable of your choosing. This
    represents one of many of your input vectors. To find your orthonormal vectors, you first take
    eachh element of the vector and divide it by the magnitude of the vector. Once that's done, we can
    repeat that step for the rest of the vectors in the matrix.

    Args:
        matrix_a: A matrix stored as a list of vectors
    
    Returns:
        An orthonormal list of vectors
    """

    result: list[list] = Stable_GS(matrix_a)[0]
    return result

#3

def conjugate_transpose(matrix_a: list[list[complex]]) -> list[list[complex]]:
    """Computes the conjugate transpose of matrix_a

    Args:
        matrix_a: A matrix stored as a list of lists
    
    Returns:
        result: The conjugate transpose of matrix_a
    """

    result: list[list[float]] = [([0] * (len(matrix_a))) for index in range(len(matrix_a[0]))]
    for column in range(len(matrix_a)):
        for row in range(len(matrix_a[0])):
            result[row][column] = matrix_a[column][row]
    return result


def matrix_identity(matrix_a):
    """Computes the identity matrix of matrix_a

    We first set up the matrix by appending a zero in each spot, then we run through the length of the
    matrix and keep replacing the zero with a one

    Args:
        matrix_a: A matrix stored as a list of lists
    
    Returns:
        new_matrix: A matrix that is the identity where the diagonal elements are all equal to one 
    """

    result: list[list[float]] = [([0] * (len(matrix_a))) for index in range(len(matrix_a[0]))]
    for element in range(len(matrix_a)):
        result[element][element] = 1
    return result


def diagonal_column(matrix_a, column_number):
    """Computes the column vector below the diagonal of our matrix_a

    Args:
        matrix_a: A matrix consisting of a list of column vectors
    
    Returns:
        The diagonal column vectors stored as a list
    """

    result: list[float] = []
    for element in range((len(matrix_a[column_number]))-column_number):
        result[element] = result.append(0)
        result[element] = matrix_a[column_number][element+column_number]
    return result

def calculate_V(element_vector, sub_X):
    
    x_norm = LA.P_norm(sub_X)
    x_element_vector = LA.sca_vec_mult(element_vector, x_norm)
    V = LA.add_vectors(x_element_vector, -sub_X)
    return V


def calculate_F(V: list[float]) -> list[list[float]]:
    """Calculates our function F which will be used to compute our Q

    First finds and uses the conjugate transpose and the dot product of our vector V for every run through
    of F, then use the function of F which is equivalent to the transpose_v multiplied by 2 which is
    then divided by the inner_v, and finally subtracts that from our I then returns the result

    Args:
        vector: Our column vector stored as a list
    
    Returns:
        F: Our function which will be used to find our Q

    """

    transpose_v: list[float] = conjugate_transpose(V)
    inner_v: float = LA.dot_product(V[0], V[0]) 
    v_multi: list[list[float]] = LA.mat_mat_mult(V, transpose_v)
    identity: list[list[int]] = matrix_identity(v_multi)
    v_matrix: list[list[float]] = LA.sca_mat_mult(v_multi, (2/inner_v))
    neg_v_matrix = LA.sca_mat_mult(v_matrix, -1)
    F: list[list[float]] = LA.add_matrix(identity, neg_v_matrix)
    return F


def calculate_Q(ID_matrix: list[list[float]], F, index) -> list[list[float]]:
    
    Q: list[list[float]] = [([0] * (len(ID_matrix))) for index in range(len(ID_matrix[0]))]
    for column in range(len(ID_matrix)):
        for row in range(len(ID_matrix[0])):
            Q[column][row] = ID_matrix[column][row]
    for column in range(len(Q)-index):
        for row in range(len(Q[0])-index):
            Q[column + index][row + index] = F[column][row]
    return Q

def calculate_QFinal(Q_list: list[list[list[float]]]):
    
    Q = Q_list[0]
    for index in range(len(Q_list) - 1):
        Q = LA.mat_mat_mult(Q, Q_list[index + 1])
    return Q


def householder(matrix_a: list[list[float]]) -> list[list[float]]:
    """Computes the full householder QR factorization

    Args:
        matrix_a: A matrix stored as a list of lists
    
    Returns:
        A list of two matrices, the first being Q, and the second being R. 

    """

    R: list[list[float]] = []
    Q_list = []
    ID_matrix = matrix_identity(matrix_a)
    for element in matrix_a:
        R.append(element)
    for index in range(len(matrix_a)-1):
        ID_matrix = matrix_identity(matrix_a)
        Ident_column = diagonal_column(ID_matrix, index)
        x: list[float] = diagonal_column(R, index)
        V: list[float] = calculate_V(Ident_column, x)
        F: list[list[float]] = calculate_F(V)
        Q: list[list[float]] = calculate_Q(ID_matrix, F, index)
        Q_list.append(Q)
        R = LA.mat_mat_mult(R, Q)

    Q = calculate_QFinal(Q_list)
    return [Q, R]

#tests
test_matrix_03 = [[1,1,1], [2,1,5]]

print(householder(test_matrix_03))