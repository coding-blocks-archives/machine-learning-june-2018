import math
import numpy as np

big = int(input("Define size for the big matrix : "))
small = int(input("Define size for the small matrix : "))
k = int(
    input(
        'Do you want to get randomised values for the matrices?Input 1 for yes '
    ))
bigMatrix = np.random.rand(
    big, big
) * 100 // 1  #Randomising two square matrices with values in between 0~99
smallMatrix = np.random.rand(small, small) * 100 // 1
if not k == 1:
    for rows in range(big):
        for columns in range(big):
            bigMatrix[rows][columns] = input(
                'Enter value for big matrix in order breadth first ')
    for rows in range(small):
        for columns in range(small):
            smallMatrix[rows][columns] = input(
                'Enter value for small matrix in order breadth first ')
print(smallMatrix)
print('-------------------------------')
print(bigMatrix)


def multiply(bigMatrix, smallMatrix, initialrow, initialcolumn):
    value = 0
    for columns in range(smallMatrix.shape[1]):
        for rows in range(smallMatrix.shape[0]):
            value = value + smallMatrix[rows][columns] * bigMatrix[initialrow +
                                                                   rows][initialcolumn
                                                                         +
                                                                         columns]
    return value

for ix in (smallMatrix):
    print(ix)
print(smallMatrix[0][0])
print(len(smallMatrix))


def multiMatrices(bigMatrix, smallMatrix):
    big = bigMatrix.shape[0]  #Getting sizes of the two square matrices
    small = smallMatrix.shape[0]
    no_of_matrices = math.ceil(big / small)**2
    #Number Of smaller matrices is square of least integer greater than/equal to size of big divided by size of small
    matrices_per_row_column = no_of_matrices**0.5
    answer = np.zeros((int(matrices_per_row_column),
                       int(matrices_per_row_column)))
    rows = 0
    initialrow = 0
    while rows < matrices_per_row_column:
        initialcolumn = 0
        columns = 0
        while columns < matrices_per_row_column:
            #print('col&row',columns,rows)
            if rows == matrices_per_row_column - 1:
                if columns == matrices_per_row_column - 1:
                    answer[rows][columns] = multiply(
                        bigMatrix, smallMatrix, (big - small), (big - small))
                else:
                    answer[rows][columns] = multiply(
                        bigMatrix, smallMatrix, (big - small), initialcolumn)
                    initialcolumn = small + initialcolumn
            else:
                if columns == matrices_per_row_column - 1:
                    answer[rows][columns] = multiply(bigMatrix, smallMatrix,
                                                     initialrow, (big - small))
                else:
                    answer[rows][columns] = multiply(bigMatrix, smallMatrix,
                                                     initialrow, initialcolumn)
                    initialcolumn = small + initialcolumn
            columns += 1
        initialrow = small + initialrow
        rows += 1
    return answer


multiMatrices(bigMatrix, smallMatrix)
