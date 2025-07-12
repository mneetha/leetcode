
def spiralOrder(matrix):
    n = len(matrix)

    # Rotate layer by layer
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first

            # Save the top element
            top = matrix[first][i]

            # Left -> Top
            matrix[first][i] = matrix[last - offset][first]

            # Bottom -> Left
            matrix[last - offset][first] = matrix[last][last - offset]

            # Right -> Bottom
            matrix[last][last - offset] = matrix[i][last]

            # Top -> Right
            matrix[i][last] = top


print(spiralOrder(matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
))
print(spiralOrder(
    matrix=[
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]
))
