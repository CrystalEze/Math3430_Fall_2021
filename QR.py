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
