import LA

#1

def Unstable_GS(matrix_a: list[list[float]]) -> list[list[float]]: 
    """Implements the unstable version of a Gram-Schmidt reduced QR factorization

    First we start by setting our three variables. Q is an empty list, V is a matrix filled with
    zeros and is the same size as matrix A, R is a matrix filled with zeros, and the v is also a float 
    equivalent to 0. After we initialize the variables, we create our first for loop which will run the length
    of matrix A. Inside that for loop, our V will be overwritten by the same Matrix A column. Inside that we'll 
    run another for loop that goes from  0 to the column. It will first override our R row and columns, or our
    inner and outer index, with our LA dot product function with our variables Q and V which represents the 
    corresponding row and column. 
    Next we will override the v with our LA scalar vector multiplication function with the variables
    Q and -R, Q representing our row and -R representing both column and row. We will then override our V[column]
    with our LA vector addition function with the variables V[column] and the float v. Our R columns will 
    then be overwritten by our LA p-norm function, which will finally be appended to our Q which is the LA 
    scalar vector multiplication function with the variables V[column] and 1 divided by the diagonal inputs of R.

    Args:
        matrix_a: A matrix which is the result of our Q and R, stored as a list of lists
    
    Returns:
        A list of two matrices, the first being Q, and the second being R
    """

    Q: list[complex or float] = []
    V: list[complex or float] = [[0,0,0], [0,0,0]] 
    R: list[complex or float] = [[0,0,0], [0,0,0]]
    v = 0

    for column in range(len(matrix_a)):
        V[column] = matrix_a[column]
        for rows in range(0, column):
            R[rows][column] = LA.dot_product(Q[rows], V[column])
            v = LA.sca_vec_mult(Q[rows], -R[rows][column])
            V[column] = LA.add_vectors(V[column], v)
        R[column][column] = LA.P_norm((V[column]))
        Q.append(LA.sca_vec_mult((V[column]), (1/R[column][column])))
    return [Q,R]


#2

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
