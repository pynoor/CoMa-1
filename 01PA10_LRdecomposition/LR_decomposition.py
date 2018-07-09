def matrixinterpreter(M):
    '''
    This function interpretes a matrix in form of a string and returns
    the matrix as a list of lists (rows)
    paramters:
        - M : Matrix in form of string
    '''
    output = M.split(", ")
    output = [line.split(" ") for line in output]
    for lineindex in range(len(output)):
        output[lineindex] = [int(x) for x in output[lineindex]]
    return output

def reversedmatrixinterpreter(matrix):
    '''
    This function interpretes a matrix in form of a list of lists and returns
    the matrix as a string
    paramteres:
        - matrix in form of a list of list
    '''
    output = []
    for i in range(len(matrix)):
        output.append(" ".join(str(x) for x in matrix[i]))
    return ", ".join(str(x) for x in output)

def LU_fuser(L, U):
    '''
    This function fuses a two matrices L and U and returns a matrix containing
    all the elements of L for i>j and all the elements of U for i<=j
    paramters:
        - Matrices L and U in form of lists of lists
    '''
    output = L
    for i in range(len(L)):
        for j in range(len(L[0])):
            if i <= j:
                output[i][j] = U[i][j]
            output[i][j] = int(output[i][j])
    return output

def LR_decomposition(M):
    '''
    This function calculates the entries of the L and U matrices
    of the LU decomposition.
    parameters:
        - Matrix M in form of list of lists
    '''
    M = matrixinterpreter(M)
    nr_lines = len(M)
    L = [[0.0 for i in range(nr_lines)] for i in range(nr_lines)]
    U = [[0.0 for i in range(nr_lines)] for i in range(nr_lines)]

    for i in range(nr_lines):
        for k in range(i, nr_lines):
            s1 = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = M[i][k] - s1

        for k in range(i, nr_lines):
            s2 = sum(L[k][j] * U[j][i] for j in range(i))
            L[k][i] = (M[k][i] - s2) / U[i][i]

    return reversedmatrixinterpreter(LU_fuser(L, U))
