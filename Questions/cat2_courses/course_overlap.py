
student_course_pairs_1 = [
  ["58", "Software Design"],
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
]


def overlap(pairs):
    course_map = dict()
    ans = dict()
    for pair in pairs:
        course_map[pair[0]] = course_map.get(pair[0], []) + [pair[1]]
    ids = list(course_map.keys())
    for i in range(len(ids)):
        for j in range(i+1, len(ids)):
            ans[(ids[i], ids[j])] = list(set(course_map[ids[i]]).intersection(course_map[ids[j]]))
    return ans

print(overlap(student_course_pairs_1))

# output = {
#     ('58', '94'): ['Economics'],
#     ('58', '17'): ['Software Design', 'Linear Algebra'],
#     ('58', '25'): ['Economics'],
#     ('94', '17'): [],
#     ('94', '25'): ['Economics'],
#     ('17', '25'): []}
# Follow up
# O(m*n+n^2), O(n)
