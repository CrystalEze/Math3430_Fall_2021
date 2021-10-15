#Problem 0

def add_vectors(vector_a: list,
                vector_b: list) -> list:
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
    
    result: list = [0 for element in vector_a]
    for index in range(len(result)):
        result[index] = vector_a[index] + vector_b[index]
    return result
print(result)
#End Problem 0