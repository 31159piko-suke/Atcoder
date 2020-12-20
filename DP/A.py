N = int(input())
l = list(map(int, input().split()))

#初期化
dp = [float('inf')]*N
dp[0] = 0
# dp[1] = abs(l[0]-l[1])

# for i in range(N-2):
#     dp[i+2] = min(abs(l[i+2]-l[i+1])+dp[i+1],abs(l[i+2]-l[i])+dp[i])


for i in range(N):
    dp[i] = min(dp[i],dp[i-1]+abs(l[i-1]-l[i]))
    dp[i] = min(dp[i],dp[i-2]+abs(l[i-2]-l[i]))



print(dp[N-1])
