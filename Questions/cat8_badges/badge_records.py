
def invalidbadge(records):
    if not records:
        return []
    state = dict()
    res = [[], []]
    invalid_enter = set()
    invalid_exit = set()

    for name, action in records:
        if name not in state:
            state[name] = 0
        if action == 'enter':
            if state[name] == 0:
                state[name] = 1
            else:
                invalid_exit.add(name)
        else:
            if state[name] == 1:
                state[name] = 0
            else:
                invalid_enter.add(name)

    for name, s in state.items():
        if s == 1:
            invalid_exit.add(name)

    for name in invalid_enter:
        res[0].append(name)

    for name in invalid_exit:
        res[1].append(name)

    return res

badge_records = [
  ["Martha",   "exit"],
   ["Paul",     "enter"],
   ["Martha",   "enter"],
   ["Martha",   "exit"],
   ["Jennifer", "enter"],
   ["Paul",     "enter"],
   ["Curtis",   "enter"],
   ["Paul",     "exit"],
   ["Martha",   "enter"],
   ["Martha",   "exit"],
   ["Jennifer", "exit"],
 ]

# [['Martha'], ['Curtis', 'Paul']]

print(invalidbadge(badge_records))

# O(n), O(n)
