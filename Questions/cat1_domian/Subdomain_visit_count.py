'''
Input:
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output:
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
'''
import collections


def SubdomainVisits(cpdomains):
    counter = collections.Counter()
    for cpdomain in cpdomains:
        count, *domains = cpdomain.replace(' ', '.').split('.')
        for i in range(len(domains)):
            counter['.'.join(domains[i:])] += int(count)
    return [str(value) + ' ' + key for key, value in counter.items()]

result = SubdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
print(result)

# O(n*k), O(n)