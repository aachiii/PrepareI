
def frequent_access(records):
    if not records:
        return []
    res = {}
    times = dict()
    for name, timestamp in records:
        if name not in times:
            times[name] = []
        times[name].append(timestamp)

    for name, t in times.items():
        if len(t) < 3:
            continue
        t.sort()
        for j in range(len(t)):
            curr = t[j]
            future = int(curr) + 100
            print(future)
            k = j

            if k+2<len(t) and int(t[k+2]) < future:
                index = k+3
                k = k+2
                while k<len(t):
                    if int(t[k]) < future:
                        index = k+1
                        k += 1
                    else:
                        break
                if name not in res:
                    res[name] = t[j:index]
                else:
                    if index-j>len(res[name]):
                        res[name] = t[j:index]
                print(t[j:index])

    print(res)



t = [['James', '1300'], ['Martha', '1600'], ['James', '1320'],['James', '1330'],['Martha', '1620'], ['Martha', '1530'], ['Martha', '1625'], ['Martha', '1700'], ['Martha', '1710'], ['Martha', '1715']]
# {'James': ['1300', '1320', '1330'], 'Martha': ['1620', '1625', '1700', '1710', '1715']}
frequent_access(t)

# O(n^2), O(n)

