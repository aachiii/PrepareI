
def get_time(meetings):
    if not meetings:
        return []
    res = []
    start = 0
    meetings = merge_meetings(meetings)
    for i in range(len(meetings)):
        res.append([start, meetings[i][0]])
        start = meetings[i][1]
    return res


def merge_meetings(meetings):
    meetings.sort()
    start, end = meetings[0]
    res = []
    for meeting in meetings:
        if end >= meeting[0]:
            end = max(end, meeting[1])
        else:
            res.append([start, end])
            start = meeting[0]
            end = meeting[1]
    res.append([start, end])
    return res


t = [[1, 3], [7, 8], [9, 10]]

print(get_time(t))

# O(n), O(n)