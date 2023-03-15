def square_matrix_simple(matrix=[]):
    # create a new matrix with the same dimensions as the input matrix
    result = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

    # iterate through the input matrix and compute the square of each integer
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] = matrix[i][j] ** 2

    # return the new matrix
    return result
