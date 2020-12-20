N = int(input())
l = list(map(int, input().split()))




#計算時間超過　方針違い
import numpy as np
dp = np.zeros((N*(N+1))//2+1)
dp[0] = 0

index = 0
for i in range(N):
    for j in range(i+1):
        index += 1
        dp[index] = dp[index-1] + l[j]
        # print(i,j,index)

print(max(dp))
