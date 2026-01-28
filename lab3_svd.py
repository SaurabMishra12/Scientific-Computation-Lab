import numpy as np


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the matrix row by row (space-separated):")

A = []
for i in range(rows):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    if len(row) != cols:
        raise ValueError("Column count mismatch")
    A.append(row)

A = np.array(A)

#Compute A^T A
ATA = A.T @ A

#Eigen decomposition of A^T A
eigenvalues, V = np.linalg.eig(ATA)

#Sort eigenvalues and eigenvectors (descending)
idx = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[idx]
V = V[:, idx]

#Singular values
singular_values = np.sqrt(np.maximum(eigenvalues, 0))

#Construct Sigma
Sigma = np.zeros((A.shape[0], A.shape[1]))
for i in range(min(len(singular_values), A.shape[0])):
    Sigma[i, i] = singular_values[i]

#Compute U
U = np.zeros((A.shape[0], len(singular_values)))
for i in range(len(singular_values)):
    if singular_values[i] != 0:
        U[:, i] = (A @ V[:, i]) / singular_values[i]

#Output
print("\nMatrix A:")
print(A)

print("\nU matrix:")
print(U)

print("\nSigma matrix:")
print(Sigma)

print("\nV^T matrix:")
print(V.T)
