A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

# Matrix addition
addition = [
    [A[i][j] + B[i][j] for j in range(2)]
    for i in range(2)
]

# Matrix multiplication
multiplication = [
    [
        sum(A[i][k] * B[k][j] for k in range(2))
        for j in range(2)
    ]
    for i in range(2)
]

print("Matrix A:")
for row in A:
    print(row)

print("Matrix B:")
for row in B:
    print(row)

print("Matrix Addition:")
for row in addition:
    print(row)

print("Matrix Multiplication:")
for row in multiplication:
    print(row)