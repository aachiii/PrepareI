def get_all_zeros(board, i, j):
    if not board:
        return False
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited = [[False for o in range(len(board[0]))] for p in range(len(board))]

    def dfs(x, y):

        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or visited[x][y] or board[x][y] == -1:
            return
        visited[x][y] = True
        for dx, dy in direction:
            x1 = x + dx
            y1 = y + dy
            dfs(x1, y1)

    dfs(i, j)
    print(visited)
    for m in range(len(board)):
        for n in range(len(board[0])):
            if board[m][n] == 0 and not visited[m][n]:
                return False
    return True


t = [[0, -1, 0, 0],
    [0, 0,  0, 0],
    [0, 0, 0, -1]]

# True

print(get_all_zeros(t, 1, 1))

# O(n), O(n)