
def find_first_c(dic):
    heads = []
    nexts = []
    for v in dic.values():
        nexts += v
    nexts = set(nexts)

    for k in dic.keys():
        if k not in nexts:
            heads.append(k)
    return heads


def solution(array):
    dic = {}
    res = []
    ans = []
    for a, b in array:
        dic[a] = dic.get(a, []) + [b]

    heads = find_first_c(dic)

    def dfs(h, path):
        if h not in dic.keys():
            res.append(path)
            return
        for i in dic[h]:
            dfs(i, path+[i])

    for head in heads:
        dfs(head, [head])
    for p in res:
        mid = (len(p)-1) // 2

        ans.append(p[mid])
    ans = list(set(ans))
    print(ans)
    return ans


all_courses = [
    ["Logic", "COBOL"],
    ["Data Structures", "Algorithms"],
    ["Creative Writing", "Data Structures"],
    ["Algorithms", "COBOL"],
    ["Intro to Computer Science", "Data Structures"],
    ["Logic", "Compilers"],
    ["Data Structures", "Logic"],
    ["Creative Writing", "System Administration"],
    ["Databases", "System Administration"],
    ["Creative Writing", "Databases"],
    ["Intro to Computer Science", "Graphics"],
]
# ['Intro to Computer Science', 'Data Structures', 'Creative Writing', 'Databases']
solution(all_courses)

# O(n), O(n)