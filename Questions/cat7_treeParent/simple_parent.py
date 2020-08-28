

def find_nodes_zero_one(edges):
    if not edges:
        return []
    dic = dict()
    res = []
    for parent, child in edges:
        if child not in dic:
            dic[child] = set()
        if parent not in dic:
            dic[parent] = set()
        dic[child].add(parent)
    print(dic)
    for key, value in dic.items():
        if len(value) == 0 or len(value) == 1:
            res.append(key)
    print(res)
    return res

test = [[1,4], [2,4], [3,5], [3,6], [4,7], [5,7], [6,8]]

#[1, 2, 5, 3, 6, 8]
# [1, 2, 5, 3, 6, 8]
print(find_nodes_zero_one(test))

# O(n), O(n)


