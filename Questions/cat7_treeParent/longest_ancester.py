
def get_last_parent(array, n, level, dic):
    parent = []
    for i in dic[n]:
        parent.append([i, level])
    if not parent:
        return parent
    else:
        next_parent = []
    for i in parent:
        next_parent += get_last_parent(array, i[0], level+1, dic)
    return parent+next_parent


def main(inputlist, n):
    dic = dict()
    for parent, child in inputlist:
        if child not in dic:
            dic[child] = set()
        if parent not in dic:
            dic[parent] = set()
        dic[child].add(parent)
    parents = get_last_parent(inputlist, n, 0, dic)
    max_level = 0
    last_parent = None

    for i in parents:
        if i[1] >= max_level:
            last_parent = i[0]
            max_level = i[1]

    print(last_parent)


main([[1,4], [2,4], [3,5], [3,6], [4,7], [5,7], [6,8]], 8)
# 3




# O(n), O(n)


