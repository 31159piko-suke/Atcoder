N,D = map(int,input().split())
l = [list(map(int,input().split())) for _ in range(N)]

import math

count = 0
for i in l:
    if math.sqrt(i[0]**2+i[1]**2)<=D:
        count += 1
print(count)
