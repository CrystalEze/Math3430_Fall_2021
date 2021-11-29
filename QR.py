import LA 

#HW05

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


#HW06

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

#HW07

def complex_con(scalar: float) -> float:
    """Computes the conjugate of the scalar by first taking our result, which is the sum of our real number
    plus our complex number multiplied by j, and returning the result

    Args:
        scalar: A scalar stored as a real and complex float
    
    Returns:
        The conjugate of the scalar
    """

    result = scalar.real + -scalar.imag*1j
    return result


def sign(s: float) -> float:
    """Calculates whether the integer is positive or negative

    If the s is greater than or equal to 0, it will return 1. If the s is less than 0, it returns -1

    Args:
        The integer, s, stored as a float
    
    Returns:
        A positive 1 or a negative 1
    """

    if s >= 0:
        return 1
    else:
        return -1


def calculate_V(Vector: list) -> list:
    """Computes the reflection of the vector

    We first inititialize our vector, denoted as c, which is equal to the range of elements in our vector.
    We then set the first index of our vector equal to 1 and use our vector addition function to add the scalar
    and vector multiplication to the product of our sign index of the vector and the p-norm of the vector

    Args:
        Vector: A vector of elements stored as a list
    
    Returns:
        The V which is the reflection vector
    
    """
    c = [0 for element in range(len(Vector))]
    c[0] = 1
    V = LA.add_vectors(Vector, LA.sca_vec_mult(c, sign(Vector[0])*LA.P_norm(Vector)))
    return V


def matrix_identity(matrix_a: int) -> int:
    """Computes the identity matrix of matrix_a

    We first set up a matrix by setting each element in the matrix equal to zero, then we run through the
    length of the matrix and keep replacing each zero with a one for the diagonal values

    Args:
        matrix_a: A matrix stored as a list of lists
    
    Returns:
        matrix_identity: The identity of the matrix
    """

    matrix_identity: list[list[float]] = [[0 for element in range(matrix_a)] for index in range(matrix_a)]
    for i in range(matrix_a):
        matrix_identity[i][i] = 1
    return matrix_identity


def deep_copy(matrix_a: list[list[float]]) -> list[list[float]]:
    """Creates a deep copy of our matrix

    First we set up a temp matrix with the same dimensions of our original matrix, then set all of the elements
    in the temp matrix equal to 0. Next, we substitute the values of our original matrix into the new matrix
    we're copying and return the temp matrix

    Args:
        matrix_a: Our resident matrix stored as a list of lists

    Returns:
        temp: A new matrix which is the deep copy of our matrix_a 
    """

    temp = [[0 for element in range(len(matrix_a[0]))] for index in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a)):
            temp[i][j] = matrix_a[i][j]
    return temp


def conjugate_transpose(matrix_a: list[list[float]]) -> list[list[float]]:
    """Computes the conjugate transpose of our input matrix
    
    First we initialize two temp matrices where all the elements of both matrices are equal to 0. Then we
    create our first for loop which makes the two temp matrices the same dimensions and takes the conjugate
    of them. Next, we create a second for loop which takes the rows and columns of our second temp matrix and
    switches them. Finally, we return our second temp matrix, which is the conjugate transpose

    Args:
        matrix_a: A matrix stored as a list of lists
    
    Returns:
        temp_02: The conjugate transpose of matrix_a
    """

    temp: list = [[0 for element in range(len(matrix_a[0]))] for index in range(len(matrix_a))]
    temp_02: list = [[0 for element in range(len(matrix_a[0]))] for index in range(len(matrix_a))]
    for i in range(len(matrix_a[0])):
        for j in range(len(matrix_a)):
            temp[i][j] = matrix_a[i][j].conjugate()
    for m in range(len(matrix_a[0])):
        for n in range(len(matrix_a)):
            temp_02[m][n] = temp[n][m]
    return temp_02


def vec_vec_mult(Vector_B: list, Vector_C: list) -> list:
    """Computes the product of two vectors

    First we initialize our result as an empty list. Next, we create our first for loop to go through each
    element in our first vector and use our scalar-vector multiplication function to multiply 
    that to the elements of the second vector and append the values to our empty list and return the result

    Args:
        Vector_B: Our first vector stored as a list
        Vector_C: Our second vector stored as a list
    
    Returns:
        The product of our two input vectors
    """

    result = []
    for i in range(len(Vector_B)):
        result.append(LA.sca_vec_mult(Vector_C, Vector_B[i]))
    return result


def calculate_F(Vector: list) -> list:
    """Computes our function F_k which will then be used to compute our Q

    First we create a scalar, h, which will equal -2 divided by the value of the p-norm of our vector squared.
    Next, we take the product of our previous two vectors and use our scalar-vector multiplication function to
    multiply it times our h and set that new matrix equal to our i. Finally, we use our matrix addition function
    to add what we got from our identity matrix function to our i and return F, which is our F_k matrix

    Args:
        Vector: Our column vector stored as a list
    
    Returns:
        F: Our F_k matrix which will be used to find our Q

    """
 
    h = -2/(LA.P_norm(Vector))**2
    i = LA.sca_mat_mult(vec_vec_mult(Vector, Vector), h)
    F = LA.add_matrix(matrix_identity(len(Vector)), i)
    return F
 

def calculate_Q(matrix_a: list[list[float]], c: int) -> list:
    """Computes the Q which will be used in the Jouseholder function

    First, we initialize an input matrix to be filled with 0's. Next, we create a for loop which first
    runs through the elements of our matrix and overwrites the indexes of our Q with our scalar integer plus the
    index, but only if the sum is less than the length of the matrix's current index. Then, we set our variable,
    v, equal to our function for finding the reflection of a vector for the parameters of the first index of our
    Q, and set another variable, f, equal to the function for finding our F_k for the parameter of our v. Next,
    we set our Q_k (this function) equal to our identity matrix function of our matrix_a and create a third
    for loop which will again overwrite the m and n of our Q_k function with the difference between our m and n
    our integer c of our f function relabeled. Finally, we return the calculated Q_k function


    Args:
        matrix_a: A matrix stored as a list of lists
        c: Represents our scalar integer

    Returns:
        Q: A matrix stored as a list of lists which will be used to calculate the householder QR factorization
    
    """
    Q: list = [[0 for n in range (c, len(matrix_a[m]))] for m in range(c, len(matrix_a))]
    for m in range(len(matrix_a)):
        for n in range(len(matrix_a[m])):
            if c + m < len(matrix_a[m]):
                 if c + n < len(matrix_a[m]):
                      Q[m][n] = matrix_a[c + m][c + n]
    
    v = calculate_V(Q[0])
    f = calculate_F(v)
    calculate_Q = matrix_identity(len(matrix_a))
    for m in range(c, len(calculate_Q)):
        for n in range(c, len(calculate_Q)):
            calculate_Q[m][n] = f[m - c][n - c]
    return calculate_Q


def Householder_QR(matrix_a: list[list]) -> list[list]:
    """Computes the full householder QR factorization

    First, it initializes R as the deep copy of matrix_a. Next, it sets the Q_list equal to an empty list. Then,
    we set our first for loop which runs through every element in our R matrix, and set the Q_k function of
    the parameters R and the index equal to the variable q, and set matrix multiplication function of the
    parameters q and R equal to our R. Next, we append our empty Q_list set to the q. We then set Q equal to the
    negated version of our Q_list and use our conjugate transpose function for the first index of our Q_list.
    We then create another for loop which starts from 1 and runs through the length of our entire Q_list. Finally,
    we set Q equal to our matrix multiplication function of our Q and the conjugate transpose function of the 
    first index of our Q_list. We then return our Q and R.
    

    Args:
        matrix_a: A matrix stored as a list of lists
    
    Returns:
        A list of two matrices, the first being Q, and the second being R. 

    """

    R: list = deep_copy(matrix_a)
    Q_list: list = []
    for index in range(len(R)):
        q: list = calculate_Q(R, index)
        R = LA.mat_mat_mult(q, R)
        Q_list.append(q)
    
    Q: list = Q_list[-1]
    Q: list = conjugate_transpose(Q_list[0])

    for element in range(1, len(Q_list)):
        Q = LA.mat_mat_mult(Q, conjugate_transpose(Q_list[element]))
    return [Q, R]


#tests
print(sign(-7))
print(calculate_V([1,2]))
print(matrix_identity(1))
print(deep_copy([[5,2],[3,4]]))
print(conjugate_transpose([[5-8j,3], [4,7-3j]]))
print(vec_vec_mult([3,6,2], [5,8,7]))
print(calculate_F([5.2,3.7]))
print(calculate_Q(calculate_F([5.2,3.7]), 1))

test_matrix_03 = [[2,2,1], [-2,1,2], [18,5,2]]
test_matrix_04 = [[1,2], [-5,2]]

print(Householder_QR(test_matrix_03))
print(Householder_QR(test_matrix_04))