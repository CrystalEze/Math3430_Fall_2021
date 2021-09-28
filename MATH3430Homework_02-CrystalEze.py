"""
Problem 00
Write an algorithm to implement vector addition
"""

#Problem 00 - Planning

"""
Q1: What do we have?

A1: Two vectors stored as lists. Denoted by the names vector_a and vector_b. 

Q2: What do we want?

A2: Their sum stored as a list.

Q3: How will we get there?

A3: We will create an empty list of the appropriate size and store the sums of
the corresponding components of vector_a and vector_b. 

-PsuedoCode

def add_vectors(vector_a,vector_b):

Initialize a result vector of 0's which is the same size as vector_a. Call this
vector result.

# Set each element of result to be equal to the desired sum.
for index in range(length(result)):
  result[index] = vector_a[index] + vector_b[index]

Return the desired result.
"""

#Problem 00 - Implementation

def add_vectors(vector_a,vector_b):
  result = [0 for element in vector_a]
  for index in range(len(result)):
    result[index] = vector_a[index] + vector_b[index]
  return result

#Problem 00 - Testing

test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]

# add_vectors(test_vector_01,test_vector_02) should output [4,3,6]
print('Test Output for add_vectors: ' + str(add_vectors(test_vector_01,test_vector_02)))
print('Should have been [4,3,6]')

test_vector_03 = [2, 4, 6]
test_vector_04 = [3, 6, 9]

# add_vectors(test_vector_03,test_vector_04) should output [5,10,15]
print('Test Output for add_vectors: ' + str(add_vectors(test_vector_03,test_vector_04)))
print('Should have been [5,10,15]')


"""
Problem 01
Write an algorith to implement scalar-vector multiplication
"""

#Problem 01 - Planning

"""
Q1: What do we have?

A1: We have a scalar and a vector, denoted as vector_a, stored in our computer as an empty list.

Q2: What do we want?

A2: We want the product of the scalar and the vector stored as a list.

Q3: How will we get there? 

A3: Create a product between the scalar and vector_a and store it in our computer as a list.

-Pseudocode

def sca_vec_mult(scalar, vector_a)

#Initialze result vector of 0's as the same size as vector_a

#Set each element of the result equal to the product
for index in range(length(result)):
    result[index] = scalar x vector_a[index]
    
#Return the desired result
"""

#Problem 01 - Implementation

def sca_vec_mult(scalar, vector_a):
    result = [0 for element in vector_a]
    for index in range(len(result)):
        result[index]= scalar*vector_a[index]
    return result

#Problem 01 - Testing

test_scalar = 5
test_vector_05 = [2,3,8]

# sca_vec_mult(test_scalar,test_vector_05) should output [10,15,40]
print('Test Output for sca_vec_mult: ' + str(sca_vec_mult(test_scalar,test_vector_05)))
print('Should have been [10,15,40]')

test_scalar = 4
test_vector_01 = [1, 2, 4]

# sca_vec_mult(test_scalar,test_vector_01) should output [4,8,16]
print('Test Output for sca_vec_mult: ' + str(sca_vec_mult(test_scalar,test_vector_01)))
print('Should have been [4,8,16]')


"""
Problem 02
Write an algorithm to implement scalar-matrix multiplication
"""

#Problem 02 - Planning

"""
Q1: What do we have?

A1: We have a scalar and a matrix, denoted as matrix_a, stored in our computer as an empty list of lists.

Q2: What do we want?

A2: We want the product of the scalar and the matrix_a.

Q3: How will we get there?

A3: We will create a product between the scalar and the matrix_a and store it in our computer as a new matrix.

-Pseudocode

def sca_mat_mult(scalar, matrix_a)

#Initialize result as an empty list

#Append 0 to the result list

#Initialize row as an empty list

#For element in rows
 Append 0 to rows

#Set each element of result to be equal to the product
for index in range(length(result)):
    result[index][row_index] = scalar*matrix_a[index][row_index]
    
#Return the desired result
"""

#Problem 02 - Implementation

def sca_mat_mult(scalar, matrix_a):
    result = []
    row = []
    for rows in matrix_a:
        row = [0 for element in rows]
        result.append (row)
    for index in range (len(result)):
        for row_index in range(len(result[index])):
           result[index][row_index] = scalar*matrix_a[index][row_index]
    return result

#Problem 02 - Testing

test_scalar_01 = 10
test_matrix_01 = [[2, 8, 7],[4, 9, 1],[10, 4, 6]]

# sca_mat_mult(test_scalar_01,test_matrix_01) should output [[20,80,70],[40,90,10],[100,40,60]]
print('Test Output for sca_mat_mult: ' + str(sca_mat_mult(test_scalar_01,test_matrix_01)))
print('Should have been [[20,80,70],[40,90,10],[100,40,60]]')

test_scalar_02 = 6
test_matrix_02 = [[2, 4, 6],[3, 6, 9],[4, 8, 12]]

# sca_mat_mult(test_scalar_02,test_matrix_02) should output [[12,24,36],[18,36,54],[24,48,72]]
print('Test Output for sca_mat_mult: ' + str(sca_mat_mult(test_scalar_02,test_matrix_02)))
print('Should have been [[12,24,36],[18,36,54],[24,48,72]]')


"""
Problem 03
Write an algorithm to implement matrix addition
"""

#Problem 03 - Planning

"""
Q1: What do we have?

A1: We have two matrices, denoted as matrix_b and matrix_c, of equal dimensions stored in our computer.

Q2: What do we want?

A2: We want the sum of matrix_b and matrix_c.

Q3: How will we get there?

A3: We will generate the sum of the two matrices by adding the element of matrix_b to the corresponding element of matrix_c. 
We will then store the result in our computer as a new matrix.

-Pseudocode

def add_matrix (matrix_b, matrix_c)

#Initialize result as an empty list

#Append 0 to the result list

#Initialize row as an empty list

#For element in rows
 Append 0 to rows
 
#Set each element of product to be equal to the sum
    for index in range(length(result)):
# For column in range(length(result[0]))
# Add the corresponding indexes of the two matrices together
# Store the desired sum as a result
# Return the desired result
"""

#Problem 03 - Implementation

def add_matrix(matrix_a, matrix_b):
    result = []
    row = []
    for rows in matrix_a:
        row = [0 for elements in rows]
        result.append (row)
    for row in range(len(matrix_a)): 
        for column in range(len(matrix_a[0])):
            result[row][column] = matrix_a[row][column]+matrix_b[row][column]
    return result

#Problem 03 - Testing

test_matrix_03 = [[2,4,6],[3,6,9]]
test_matrix_04 = [[4,8,12],[5,10,15]]

# add_matrix(test_matrix_03,test_matrix_04) should output [[6,12,18],[8,16,24]]
print('Test Output for add_matrix: ' + str(add_matrix(test_matrix_03,test_matrix_04)))
print('Should have been [[6,12,18],[8,16,24]]')

test_matrix_05 = [[1, 2, 4],[2, 6, 8]] 
test_matrix_06 = [[5, 2, 4],[3, 8, 7]]

# add_matrix(test_matrix_05,test_matrix_06) should output [[6,4,8],[5,14,15]]
print('Test Output for add_matrix: ' + str(add_matrix(test_matrix_05,test_matrix_06)))
print('Should have been [[6,4,8],[5,14,15]]')


"""
Problem 04
Write an algorithm to implement matrix-vector multiplication using the linear
combination of columns method
"""

#Problem 04 - Planning

"""
Q1: What do we have?

A1: We have a matrix whose columns matches the number of rows in our vector stored in our computer. 
We will denote them as matrix_c and vector_d.

Q2: What do we want?

A2: We want the product multiplication of the matrix and the vector.

Q3: How will we get there?

A3: First we will multiply the first column of the matrix by the first row of the vector. We will do this with the following
columns and rows until all the elements have been multiplied. Then we will store our result as a new vector in our computer.

-Pseudocode

def mat_vec_mult (matrix_c, vector_d)

#Initialize a result vector of 0's which is the same size as the matrix list

#For each matrix list write as result of sca_vec_mult(scalar, vector_a)

#For each matrix list, set the result equal to result plus the list

#Return the desired result
"""

#Problem 04 - Implementation

def mat_vec_mult (matrix_c, vector_d):
    result = []
    for index in range (len(vector_d)):
        result = [0 for element in vector_d]
    for index in range (len(vector_d)):
        temp = sca_vec_mult(vector_d[index], matrix_c[index])
        for m in range (len(temp)):
            result[m] = result[m] + temp[m]
    return result

#Problem 04 - Testing

test_vector_06 = [2,4,6]
test_matrix_07 = [[3,4,6],[8,7,2],[9,12,8]]

# mat_vec_mult(test_vector_06,test_matrix_07) should output [92,108,68]
print('Test Output for mat_vec_mult: ' + str(mat_vec_mult(test_vector_06,test_matrix_07)))
print('Should have been [[92,108,68]]')

test_vector_07 = [1, 4, 7]
test_matrix_08 = [[5, 6, 5],[2, 8, 4],[7, 6, 1]]

# mat_vec_mult(test_vector_07,test_matrix_08) should output [62,80,28]
print('Test Output for mat_vec_mult: ' + str(mat_vec_mult(test_vector_07,test_matrix_08)))
print('Should have been [62,80,28]')


"""
Problem 05
Write an algorithm to implement matrix-matrix multiplication
"""

#Problem 05 - Planning

"""
Q1: What do we have?

A1: We have two matrices, denoted as matrix_e and matrix_f, of equal dimensions stored in our computer.

Q2: What do we want?

A2: We want the desired product of the two matrices.

Q3: How will we get there?

A3: First we will multiply the first index in the first column of matrix_e
by the corresponding index in the first row of matrix_f and add them together. We will continue
this process until all elements of the matrices have been calculated. Then we will store the result as a 
new matrix in our computer.

-Pseudocode

def mat_mat_mult(matrix_e, matrix_f)

#Initialize an empty list called result

#For each index in matrix_f append the result of (mat_vec_mult(matrix_e, index)) back into the result

#Return the desired result
"""

#Problm 05 - Implementation

def mat_mat_mult (matrix_e, matrix_f):
    result = []
    for index in matrix_f:
        result.append(mat_vec_mult(matrix_e, index))
    return result

#Problem 05 - Testing

test_matrix_09 = [[2, 4],[3,6]] 
test_matrix_10 = [[3, 9],[4, 8],[6,1]]

# mat_mat_mult(test_matrix_09,test_matrix_10) should output [[33,66].[32,64],[15,30]]
print('Test Output for mat_mat_mult: ' + str(mat_mat_mult(test_matrix_09,test_matrix_10)))
print('Should have been [[33,66],[32,64],[15,30]]')

test_matrix_11 = [[4, 10],[5, 20]]
test_matrix_12 = [[8, 6],[9, 10]]

# mat_mat_mult(test_matrix_11,test_matrix_12) should output [[62,200],[86,290]]
print('Test Output for mat_mat_mult: ' + str(mat_mat_mult(test_matrix_11,test_matrix_12)))
print('Should have been [[62,200],[86,290]]')

