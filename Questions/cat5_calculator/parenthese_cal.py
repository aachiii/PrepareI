
def calculate(ss):
    if not ss:
        return 0
    num = 0
    sign = 1
    stack = []
    res = 0
    for s in ss:
        if s.isdigit():
            num = num*10+int(s)
        elif s in ('+', '-'):
            res += sign*num
            num = 0
            sign = 1 if s == '+' else -1
        elif s == '(':
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif s == ')':
            res += sign*num
            sign = stack.pop()
            res += sign*stack.pop()
            num = 0
    return res


a = "2+((8+2)+(3-999))"
print(calculate(a))

# O(n), O(n)

