
def find_circles(array):
    if not array:
        return None
    dic = {}
    res = [array[0][0]]
    for i, j in array:
        if i not in dic:
            dic[i] = {}
        if j not in dic:
            dic[j] = {}
        dic[i][j] = False
        dic[j][i] = False
    prev = array[0][0]
    for i in range(len(array)-1):
        if prev in dic:
            for k, v in dic[prev].items():
                if not v:
                    res.append(k)
                    dic[prev][k] = True
                    dic[k][prev] = True
                    prev = k
                    break
    print(res)


b = [[3, 5], [1, 4], [2, 4], [1, 5], [2, 3]]
find_circles(b)
