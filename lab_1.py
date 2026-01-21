# Read matrix dimensions
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Read matrix
matrix = []
print("Enter the matrix row by row (space separated):")

for i in range(rows):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    matrix.append(row)

# Gaussian Elimination with Pivoting
for i in range(rows):

    # If pivot is zero, swap with a lower row
    if matrix[i][i] == 0:
        for k in range(i + 1, rows):
            if matrix[k][i] != 0:
                matrix[i], matrix[k] = matrix[k], matrix[i]
                print(f"Swapped Row {i+1} with Row {k+1}")
                break
        else:
            print("No valid pivot found. System may have no unique solution.")
            exit()

    # Normalize pivot row
    pivot = matrix[i][i]
    for j in range(cols):
        matrix[i][j] /= pivot

    # Eliminate entries below pivot
    for k in range(i + 1, rows):
        factor = matrix[k][i]
        for j in range(cols):
            matrix[k][j] -= factor * matrix[i][j]

# Print result
print("\nMatrix after Gaussian Elimination:")
for row in matrix:
    print(row)