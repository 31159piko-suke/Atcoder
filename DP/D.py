N,W = list(map(int, input().split()))
l = [list(map(int, input().split())) for _ in range(N)]

import numpy as np

dp = np.zeros((N+1,W+1))
dp[0][0] = 0


for i in range(0,N):
    for j in range(0,W+1):
        if j>=l[i][0]:
            dp[i+1][j] = max(dp[i][j],dp[i][j-l[i][0]]+l[i][1])
        else:
            dp[i+1][j] = dp[i][j]

print(int(max(dp[N])))
print(dp)
