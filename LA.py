#0

def add_vectors(vector_a: list[float], vector_b: list[float]) -> list[float]:
    """Adds the two input vectors
    
    Creates a result vector stored as a list of 0's the same length as the input 
    then overwrites each element of the result vector with the corresponding
    element of the sum of the input vectors. Achieves this using a for loop over
    the indices of result. 
    
    Args:
        vector_a: A vector stored as a list.
        vector_b: A vector, the same length as vector_a, stored as a list.
        
    Returns:
        The sum of the input vectors stored as a list.
    """

    result: list[float] = [0 for element in vector_a]
    for index in range(len(result)):
        result[index] = vector_a[index] + vector_b[index]
    return result


#1 

def sca_vec_mult(Vector: list[float], Scalar: float) -> list[float]:
    """Multiplies the input scalar and the vector

    Creates an empty set whose elements are the zero elements in the given vector
    which is either increased or decreased by the scalar input.

    Args:
        Vector: A vector stored as a list
        Scalar: A scalar stored as a float
    
    Returns:
        The product of the input scalar and the vector stored as a list.
    """
    result: list[float] = []
    for index in range(len(Vector)):
        result.append(Vector[index]*Scalar)
    return result


def absolute(scalar: complex or float) -> complex or float:
    """Takes a scalar stored as a complex number or a float as the input

    Creates a scalar of a positive or negative value and takes the absolute value of it.

    Args:
        Scalar: A scalar stored as a complex number or float
    
    Returns:
        The absolute value of the scalar
    """
    return(scalar.real**2 + scalar.imag**2)**(1/2)

#tests
test_scalar_a = -5j
test_scalar_b = -16j

print(absolute(test_scalar_a))
print(absolute(test_scalar_b))


#2

def sca_mat_mult(matrix_a: list[list[float]], scalar: float) -> list[list[float]]:
    """Multiplies the input scalar and the input matrix
    
    Creates an empty set whose elements are the zeero elements in the matrix which
    is either increased or decreased by the scalar input.

    Args:
        matrix_a: A matrix stored as a list of lists
        scalar: A scalar stored as a float

    Returns:
        The product of the input scalar and the input matrix.
    """
    result: list[float] = []
    for index in range(len(matrix_a)):
        result.append(sca_vec_mult(matrix_a[index], scalar))
    return result


def P_norm(vector:list[float], p:int = 2) -> float:
    """Calculates the p-norm of the vector

    Creates a result vector first, then runs through each element of the vector taking the
    absolute value and raising it each to the power p. It then adds them all together and
    takes the p root of the sums, substituting it into the result vector

    Args:
       vector: A vector stored as a list
       p: A scalar valued as a float, set to a default of 2

    Returns:
        The p-norm of the input vector
    """
    result: float = 0
    for element in vector:
        result += element**(abs(p))
    return result**(abs(1/p))

#tests
test_vector_a = [-3, 4]
test_vector_b = [6, -8]

print(P_norm(test_vector_a))
print(P_norm(test_vector_b))


#3

def add_matrix(matrix_a: list[list[float]], matrix_b: list[list[float]]) -> list[list[float]]:
    """Adds the two input matrices

    Creates an empty list of lists with zeros then overwrites each element with 
    its corresponding sum from the input matrices

    Args:
        matrix_a: A matrix stored as a list of lists
        matrix_b: A matrix which is the same length as matrix_a, stored as a list of lists

    Returns:
         The sum of the two input matrices
    """
    result: list[list[float]] = []
    for index in range(len(matrix_a)):
        temp = add_vectors(matrix_a[index], matrix_b[index])
        result.append(temp)
    return result


def Infinity_norm(vector: list[float]) -> float:
    """Calculates the infinity norm of the vector
       
    Creates a result vector first, then runs through each element of the vector, then takes the
    absolute value of each number and equates to the result value. It then replaces the current values
    and checks if the absolute value is greater than the previous values. If it is, then that number is
    the infinity norm and we set it equal to the result

    Args:
       vector: A vector stored as a list of real and complex numbers

    Returns:
         The infinity norm of the vector
    """
    result: list[float] = 0
    numb = 0
    for element in vector:
        numb = abs((element))
        if numb > result:
            result = numb
    return result

#tests
test_vector_c = [7, 6, 1]
test_vector_d = [3, 9, 4]

print(Infinity_norm(test_vector_c))
print(Infinity_norm(test_vector_d))


#4

def mat_vec_mult(Matrix: list[list[float]], Vector: list[float]) -> list[float]:
    """Multiplies the input vector and the input matrix

    Creates a zero vector the same size as the column of the matrix
    then overwrites each element with its corresponding product from
    the column vector, multiplied by the corresponding column of the
    matrix. It then adds the elements of the columns to give us the new elements which will replace the zero
    vector.

    Args:
        Matrix: A matrix stored as a list of lists
        Vector: A vector stored as a list
    
    Returns:
        The product of the input vector and the input matrix
    """
    result: list[float] = [0 for element in Matrix]
    for index in range(len(Vector)):
        result[index] = sca_vec_mult(Matrix[index], Vector[index])
    temp = add_vectors(result[0], result[1])
    for index in range(2, len(result)):
        temp = add_vectors(temp, result[index])
    return temp


def Input_Vector(vector: list[float], p: int = 2, b: bool = False) -> float:
    """Calculates either the p-norm or the infinity norm depending on the true/false statement

    If the boolean value is true, the function result will be the infinity norm of the
    input vector and will return it as such. If the boolean value is false, it will be 
    the p-norm of and will return it as such.

    Args:
        vector: A vector stored as a list
        p: A scalar valued as a float, set to a default of 2
        b: A boolean value, set as a default of False

    Reurns:
        A float which is either the infinity norm or the p-norm of the vector
    """
    if (b == False):
        return P_norm(vector, p)
    else:
        return Infinity_norm(vector)

#tests
test_vector_e = [5, -12]
test_vector_f = [-13, -6]

print(Input_Vector(test_vector_e, 2, True))
print(Input_Vector(test_vector_f, 2, True))


#5

def mat_mat_mult(Matrix_E: list[list[float]], Matrix_F: list[list[float]]):
    """Multiplies the two input matrices

    Creates a zero matrix whose dimensions are the same size as the matrix its being
    multiplied by, then overwrites each of the elements with its corresponding product 
    from the first matrix's row, multiplied by the corresponding column of the second
    matrix. It then adds the elements of the corresponding products, to give us the new 
    elements which will replace the zero matrix.

    Args:
        Matrix_E: A matrix stored as a list of lists
        Matrix_F: A matrix, the same size as Matrix_E, stored as a list of lists
    
    Returns:
         The product of the two input matrices
    """
    result: list[list[float]] = []
    for index in range(len(Matrix_F)):
        result.append(mat_vec_mult(Matrix_E, Matrix_F[index]))
    return result


def dot_product(vector_01: list[complex or float], vector_02: list[complex or float]) -> complex or float:
    """Calculates the dot product of the two input vectors

    Creates a result float first, then runs through each of the two vectors. If the 
    vectors have complex numbers, it will take the conjugate of it first before multiplying
    the element of the first vector with the corresponding element of the second vector and adding
    them up together.

    Args:
        vector_01: A vector stored as list of real or complex numbers
        vector_02: Another vector stored as list of real or complex numbers
    
    Returns:
        The inner product, or the dot product of the two vectors
    """
    result: complex or float = 0
    for i in range(len(vector_01)):
        result += vector_01[i]*vector_02[i]
    return result

#tests
test_vector_g = [7, 0, -2j]
test_vector_h = [1, -1j, 4]
test_vector_i = [-3, 2, 9]
test_vector_j = [-8, 4, 6]

print(dot_product(test_vector_g, test_vector_h))
print(dot_product(test_vector_i, test_vector_j))