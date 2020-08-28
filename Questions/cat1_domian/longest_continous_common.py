'''
[
  ["3234.html", "xys.html", "7hsaa.html"], // user1
  ["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"] // user2
]

["xys.html", "7hsaa.html"]
'''


def solution(users):
    if len(users) != 2: return []
    user1, user2 = users
    if len(user1) == 0 or len(user2) == 0:
        return []
    length = 0
    maps = [[0 for _ in range(len(user2)+1)] for p in range(len(user1)+1)]
    res = []
    # print(maps)
    for i in range(1, len(user1)+1):
        for j in range(1, len(user2)+1):
            if user1[i-1] == user2[j-1]:
                maps[i][j] = maps[i-1][j-1] + 1
                if maps[i][j] > length:
                    res = user2[j-maps[i][j]:j]

    return res

# meet same item
# continue to end or not same
result = solution([["3234.html", "xys.html", "7hsaa.html", 'xy', 'z', "7hsaa.html", 'xy', 'z'], ["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html", 'xy', "7hsaa.html", 'xy', 'z']])
# result = solution([["3234.html"], []])

# O(mn), O(mn)

print(result)
