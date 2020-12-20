N = int(input())
l = list(map(int, input().split()))

import itertools

count = 0
for hen in itertools.combinations(l, 3):
    hen = list(hen)
    if hen[0]!=hen[1] and hen[1]!=hen[2] and hen[2]!=hen[0]:
        max_ = max(hen)
        # hen.pop(hen.index(max(hen)))
        hen.remove(max(hen))
        sum_ = sum(hen)
        if  max_ < sum_:
            count += 1
print(count)
