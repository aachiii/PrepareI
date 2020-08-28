
def has_common_ancestor(edges, x, y):
    if not edges:
        return False
    dic = dict()
    for parent, child in edges:
        if child not in dic:
            dic[child] = set()
        if parent not in dic:
            dic[parent] = set()
        dic[child].add(parent)
    x_set = find_all_parents(dic, x)
    y_set = find_all_parents(dic, y)
    print(x_set)
    print(y_set)
    return True if x_set.intersection(y_set) else False


def find_all_parents(dic, x):
    res = {x}
    stack = [x]
    while stack:
        curr = stack.pop()
        parents = dic[curr]
        for p in parents:
            res.add(p)
            stack.append(p)
    return res


test = [[1,4], [2,4], [3,5], [3,6], [4,7], [5,7], [6,8]]
print(has_common_ancestor(test, 7, 8))

# O(n) O(n)