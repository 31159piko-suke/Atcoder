N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]


dp = [[0 for j in range(3)] for i in range(3)]

import numpy as np
dp = np.zeros((3, 3))#こっちのほうがいいかな

#これだと補完機能でへんになるからだめ  オブジェクト指向理解しよう！
# dp[0][0] = l[0][0]
# dp[0][1] = l[0][1]
# dp[0][2] = l[0][2]
dp[0] = l[0]

for i in range(N):#日数
    for j in range(N):#a,b,c
        for k in range(N):
            if j!=k:
                dp[i][j] = max(dp[i][j],dp[i-1][k]+l[i][j])

f_max = max(dp[N-1][0],dp[N-1][1],dp[N-1][2])

print(int(f_max))
