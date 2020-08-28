
def can_schedule(meetings, start, end):
    for meeting in meetings:
        s, e = meeting[0], meeting[1]
        if (s <= start < e) or (s < end <= e) or (start < s and end > e):
            return False
    return True

t = [[1300, 1500], [930, 1200], [830, 845]]
# return False

print(can_schedule(t, 1450, 1500))

# O(n), O(1)