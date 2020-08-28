
def basic_calculator(expression):
    if not expression:
        return 0
    res = 0
    sign = 1
    num = 0
    for e in expression:
        if e.isdigit():
            num = num*10 + int(e)
        else:
            res += sign*num
            num = 0
            if e == '-':
                sign = -1
            else:
                sign = 1
    if num != 0:
        res += sign*num
    return res


s = "-2+3"
print(basic_calculator(s))

# O(n), O(1)