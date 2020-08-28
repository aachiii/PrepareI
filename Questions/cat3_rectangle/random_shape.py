
def find_multiple(board):
    if not board or len(board) == 0 or len(board[0]) == 0:
        return []
    res = []
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(x, y, shape):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return
        if board[x][y] == 0:
            shape.append([x, y])
            board[x][y] = 1
            for dx, dy in direction:
                dfs(x+dx, y+dy, shape)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                shape = []
                dfs(i, j, shape)
                res.append(shape)
    return res


test = [[1,1,1,1,1],
[1,0,0,1,1],
[1,0,0,1,1],
[1,1,0,1,0]]

# [[[1, 1], [2, 1], [2, 2], [3, 2], [1, 2]], [[3, 4]]]
print(find_multiple(test))

# O(n), O(n)
