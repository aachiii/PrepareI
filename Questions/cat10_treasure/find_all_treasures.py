
def find_all_treasures(board, start, end):
    if not board:
        return None
    num_treasures = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                num_treasures += 1

    paths = []

    def dfs(x, y, path, remain_t):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] == -1 or board[x][y] == 2:
            return
        path.append([x, y])
        temp = board[x][y]
        if temp == 1:
            remain_t -= 1
        if x == end[0] and y == end[1] and remain_t == 0:
            paths.append(path.copy())
            path.pop()
            board[x][y] = temp
            return
        board[x][y] = 2
        dfs(x+1, y, path, remain_t)
        dfs(x-1, y, path, remain_t)
        dfs(x, y+1, path, remain_t)
        dfs(x, y-1, path, remain_t)
        board[x][y] = temp
        path.pop()

    dfs(start[0], start[1], [], num_treasures)
    if len(paths) == 0:
        return []
    min_paths = len(paths[0])
    res = paths[0]
    for i in range(len(paths)):
        if min_paths > len(paths[i]):
            min_paths = len(paths[i])
            res = paths[i]
    print(res)
    return res

board3 = [
    [  1,  0,  0, 0, 0 ],
    [  0, -1, -1, 0, 0 ],
    [  0, -1,  0, 1, 0 ],
    [ -1,  0,  0, 0, 0 ],
    [  0,  1, -1, 0, 0 ],
    [  0,  0,  0, 0, 0 ],
]

find_all_treasures(board3, [0, 0], [4, 1])

# O(n^2), O(n^2)