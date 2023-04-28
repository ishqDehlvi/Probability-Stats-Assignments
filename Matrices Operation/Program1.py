# Aim: To declare two matrices and perform arithmetic operations

import numpy as np

matrice1 = np.array([[10,20,30],[40,50,60],[70,80,90]])
matrice2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

# Addition of Matrices
print("matrice1 + matrice2")
print(matrice1+matrice2)

print("added matrix using numpy:")
print(np.add(matrice1,matrice2))
print()

# Subtraction of Matrices
print("matrice1 - matrice2")
print(matrice1-matrice2)

print("subtracted matrix using numpy:")
print(np.subtract(matrice1,matrice2))
print()

# Division of Matrices
print("matrice1 / matrice2")
print(matrice1/matrice2)

print("divided matrix using numpy:")
print(np.divide(matrice1,matrice2))
print() 

# Multiplication of Matrices
print("matrice1 * matrice2")
print(matrice1*matrice2)

print("multiplied matrix using numpy:")
print(np.multiply(matrice1,matrice2))
print()