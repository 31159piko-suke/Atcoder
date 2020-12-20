H,W,K = map(int,input().split())
l = [list(input()) for _ in range(H)]

import copy
import collections
import numpy as np
import itertools


gyou = [i for j in range(H+1) for i in itertools.combinations(list(range(H)),j)]
retu = [i for j in range(W+1) for i in itertools.combinations(list(range(W)),j)]
#全部のっくみあわせのリストを作成して、for分でしらみつぶしにしていく

count = 0

for i in gyou:
    for j in retu:
        l_copy = np.array(copy.deepcopy(l))
        l_copy[i,:] = 0
        l_copy[:,j] = 0
        num_b = 0
        for k in range(H):
            num_b += collections.Counter(l_copy[k])["#"]
        if num_b == K:
            count += 1

print(count)
