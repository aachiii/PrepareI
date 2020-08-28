
def get_cordinates(board):
    if not board or len(board) == 0 or len(board[0]) == 0:
        return []
    row = len(board)
    col = len(board[0])
    res = []

    for r in range(row):
        for c in range(col):
            if board[r][c] == 0:
                res.append([r, c])
                bottom = r
                while bottom < row and board[bottom][c] == 0:
                    bottom += 1
                bottom -= 1
                right = c
                while right < col and board[bottom][right] == 0:
                    right += 1
                right -= 1
                res.append([bottom, right])
                return res

    return res


test = [[1,1,1,1,1],
[1,0,0,1,1],
[1,0,0,1,1],
[1,1,1,1,1]]

ans = get_cordinates(test)
#[[1, 1], [2, 2]]
print(ans)

# O(n), O(1)
