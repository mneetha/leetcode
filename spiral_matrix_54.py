

def spiralOrder(matrix):
    m = len(matrix)
    n= len(matrix[0])
    i,j = 0 ,0
    k = 1

    while i < m and j < n:
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")
        j = j+k
        if j in [0,n-1]:
            print(f"matrix[{i}][{j}] = {matrix[i][j]}")
            i = i + 1
            k = -k


print(spiralOrder(matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
))
print(spiralOrder(matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
