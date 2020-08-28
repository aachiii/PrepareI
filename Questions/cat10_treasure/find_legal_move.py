
def find_legal_moves(board, i, j):
    if not board:
        return []
    res = []
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for dx, dy in direction:
        x = i + dx
        y = j + dy
        if board[x][y] == 0:
            res.append([x, y])
    return res


t = [[0, -1, 0, 0],
    [0, 0,  -1, 0],
    [0, 0, 0, -1]]

print(find_legal_moves(t, 1, 1))

# O(1), O(1)