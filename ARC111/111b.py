N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]

import numpy as np
import itertools
import collections

lf = list(itertools.chain.from_iterable(l))
lf = np.array(lf)

l_1 = []
for i in range(N):
    l_1.append(l[i][0])


c_1 = collections.Counter(l_1)
set_1 = set(l_1)

print(np.array(c_1.values())==1)



# l_2 = []
# for i in range(N):
#     l_2.append(l[i][1])


# c_2 = collections.Counter(l_2)
# set_2 = set(l_2)


# set_ = set_2 - set_1




# count = 0
# for i in in (list(set_)):

    

# print(len(set_1)+count)





# (np.array((np.where(lf==i)))-1)[0]


# l = sorted(list(itertools.chain.from_iterable(l)))
# c = collections.Counter(l)

# print(l)
# print(c)