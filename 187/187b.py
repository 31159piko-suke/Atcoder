N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]

import numpy as np
l = np.array(l)

result = 0

for i in range(N):
    l_list = l-l[i]
    # print(l_list)
    for j in range(N):
        if l_list[j][0]==0:
            pass
        elif abs(l_list[j][1]/l_list[j][0])<=1:
            result += 1
print(result//2)