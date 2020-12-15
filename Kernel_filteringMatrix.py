import numpy as np


def multiply (big_matrix , small_matrix):
    
    temp1 = np.subtract((big_matrix.shape),(small_matrix.shape))
    temp =  np.add((temp1),([1,1]))    
    

    x , y = small_matrix.shape[0],small_matrix.shape[1]
    final_matrix = np.zeros(temp)
    
    for i in range(temp[0]):
        for j in range(temp[1]):
            c = big_matrix[i:i+x , j:j+y]
            element_product = np.multiply(c, small_matrix)
            final_matrix[i][j] = np.sum(element_product)
    return final_matrix


a = input()

b= input()

print multiply(b,a)
# [[2,3,1],[4,2,1],[1,3,2]]
# [[1,2],[3,4]]





