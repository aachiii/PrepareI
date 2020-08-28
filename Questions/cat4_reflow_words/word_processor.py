
def reflow(lines, maxlen):
    if not lines or maxlen <= 0:
        return []
    res = []
    words = ' '.join(lines).split(' ')
    each_line = []
    i = 0
    while i < len(words):
        remain = maxlen
        one = []
        while i < len(words) and remain and len(words[i]) <= remain:
            one.append(words[i])
            remain -= (len(words[i]) + 1)
            i += 1
        each_line.append((one, remain+1))
    print(each_line)
    for i in range(len(each_line)):
        if i == len(each_line)-1:
            res.append('-'.join(each_line[i][0]))
        else:
            need = each_line[i][1]
            word_array = each_line[i][0]
            ans = ''
            seat = ['-' for i in range(len(word_array)-1)]
            # seat[-1] = ''

            ave, mod = divmod(need, len(seat))
            for j in range(len(seat)):
                seat[j] += '-'*ave
            for j in range(mod):
                seat[j] += '-'

            for k in range(len(word_array)):
                if k == len(word_array)-1:
                    ans += word_array[k]
                else:
                    ans += word_array[k]
                    ans += seat[k]
            res.append(ans)
    return res





a = [ "The day began as still as the",
          "night abruptly lighted with",
          "brilliant flame" ]
#[ "The--day--began-as-still",
          # "as--the--night--abruptly",
          # "lighted--with--brilliant",
          # "flame" ]
print(reflow(a, 24))

# O(n^2), O(n)