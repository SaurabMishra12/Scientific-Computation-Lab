import numpy as np

n = int(input("Enter matrix size (n x n): "))

print("Enter matrix row by row:")
A = []
for _ in range(n):
    A.append(list(map(float, input().split())))

A = np.array(A, dtype=float)


L = np.zeros((n, n)) #initiLISING L and U matrix
U = np.zeros((n, n))

for i in range(n):
    L[i, i] = 1

    
    for j in range(i, n):
        U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i)) # computing u

    if U[i, i] == 0:
        print("Zero pivot!!!") # fails
        exit()

    # Compute L
    for j in range(i+1, n):
        L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]

print("\nL matrix:")
print(L)

print("\nU matrix:")
print(U)

print("\nChecking conditions: A = LU", np.allclose(A, L @ U))
