
def is_valid_nonogram(matrix, rows, cols):
    if not matrix or not rows or not cols:
        return False
    n = len(matrix)
    m = len(matrix[0])

    if n == 0 or n != len(rows) or m != len(cols):
        return False
    return is_rows_valid(matrix, rows, n, m) and is_cols_valid(matrix, cols, n, m)


def is_rows_valid(matrix, rows, n, m):
    for i in range(n):
        j = 0
        r = 0
        while j < m:
            if matrix[i][j] == 0:
                if len(rows[i]) == 0:
                    return False
                span = 1
                j += 1
                while j < m and matrix[i][j] == 0:
                    span += 1
                    j += 1
                if rows[i][r] != span:
                    return False
                r += 1
            j += 1
    return True


def is_cols_valid(matrix, cols, n, m):
    for i in range(m):
        j = 0
        r = 0
        while j < n:
            if matrix[j][i] == 0:
                if len(cols[i]) == 0:
                    return False
                span = 1
                j += 1
                while j < n and matrix[j][i] == 0:
                    span += 1
                    j += 1
                if cols[i][r] != span:
                    return False
                r += 1
            j += 1
    return True





#########
matrix1 = [[1, 1, 1, 1],
           [0, 1, 1, 1],
           [0, 1, 0, 0],
           [1, 1, 0, 1],
           [0, 0, 1, 1]]

rows1_1 = [[],[1],[1,2],[1],[2]]
columns1_1 = [[2,1],[1],[2],[1]]
##########

##########
matrix2 = [
    [1,1],
    [0,0],
    [0,0],
    [1,0]
]
# False
rows2_1 = [[],[2],[2],[1]]
columns2_1 = [[1,1],[3]]
##########

res = is_valid_nonogram(matrix1, rows1_1, columns1_1)
print(res)

res2 = is_valid_nonogram(matrix2, rows2_1, columns2_1)
print(res2)

# O(mn), O(1)