rows = int(input("Enter number of rows: ")) #takes input (dim)
cols = int(input("Enter number of columns: "))


matrix = []  # a list to store the matrix
print("Enter the matrix row by row (space separated):")

for i in range(rows):  # reading matrix elements row by row and performs split based on space the append to dedicated row 
    row = list(map(float, input(f"Row {i+1}: ").split()))
    matrix.append(row)


for i in range(rows):  # start gaussian elimination performs forward pass
    pivot = matrix[i][i] #now we ll make the diagonal elemnts 1 
    for j in range(cols):
        matrix[i][j] = matrix[i][j] / pivot

   
    for k in range(i + 1, rows): #making elements below the pivot 0
        factor = matrix[k][i]
        for j in range(cols):
            matrix[k][j] = matrix[k][j] - factor * matrix[i][j]


print("\nMatrix after Gaussian Elimination:") #showing the matrix 
for row in matrix:
    print(row)
