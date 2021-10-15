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
    """Multiplies thr input scalar and the vector

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

