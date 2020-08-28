
def is_valid_matrix(matrix):
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    n = len(matrix)
    rowset = [set() for _ in range(n)]
    colset = [set() for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if 1 <= matrix[i][j] <= n:
                if matrix[i][j] not in rowset[i]:
                    rowset[i].add(matrix[i][j])
                else:
                    return False
                if matrix[i][j] not in colset[j]:
                    colset[j].add(matrix[i][j])
                else:
                    return False
            else:
                return False
        
    return True


test1 = [[1,3,2],
[2,1,3],
[3,2,1]]

# True
# False

test2 = [[1,2,3],
[1,2,3],
[1,2,3]
]

print(is_valid_matrix(test1))
print(is_valid_matrix(test2))

# O(n^2), O(n)

