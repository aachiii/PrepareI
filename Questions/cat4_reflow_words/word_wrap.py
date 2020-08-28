
def word_wrap(words, maxlen):
    if not words or maxlen <= 0:
        return []
    res = []
    i = 0
    while i < len(words):
        remain = maxlen
        count = 0
        while i < len(words):
            if remain - len(words[i]) < 0:
                break
            count += 1
            remain -= len(words[i]) + 1
            i += 1
        res.append('-'.join(words[i-count:i]))
    print(res)


# O(n), O(n)
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# ['a-b-c', 'd-e-f', 'g']
word_wrap(a, 3)

b = ["1p3acres", "is", "a", "good", "place", "for", "communicate"]
word_wrap(b, 12)

