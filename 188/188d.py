N,C = map(int,input().split())
l = [list(map(int,input().split())) for i in range(N)]
import numpy as np
import itertools

max_b = max(np.array(l)[:, 1])
print(max_b)

print(l)
higoto = [0] * (max_b+1)

for i in range(N):
    higoto[l[i][0]-1] += l[i][2]
    higoto[l[i][1]] -= l[i][2]
    
new_l = np.array(list(itertools.accumulate(higoto)))

new_l = np.where(new_l < C, new_l, C)

print(np.sum(new_l))
