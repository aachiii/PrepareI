
def solution(array):
    mid = len(array) // 2
    dic = dict()
    for a, b in array:
        dic[a] = b
    values = set(dic.values())

    head = array[0][0]
    for k in dic.keys():
        if k not in values:
            head = k
            break

    for i in range(mid):
        head = dic[head]
    return head

a = [['A', 'B'], ['C', 'D'], ['B', 'C'], ['E', 'F'], ['D', 'E']]
# output C
print(solution(a))

# O(n), O(n)