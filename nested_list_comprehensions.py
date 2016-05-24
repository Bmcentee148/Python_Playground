# Create a 3x4 matrix using a list of lists
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [4, 3, 2, 1]
]

# Create transpose of the matrix using nested list comprehension
transpose = [[row[i] for row in matrix] for i in range(4)]
print transpose

# Create transpose now using a single comprehension and a loop
transpose_again = []
for i in range(4) :
    transpose_again.append([row[i] for row in matrix])
print transpose_again

# Create transpose using a good old, long ass nested loop
transpose_thrice = []
for i in range(4) :
    transposed_row = []
    for row in matrix :
        transposed_row.append(row[i])
    transpose_thrice.append(transposed_row)
print transpose_thrice