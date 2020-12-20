N,M = list(map(int, input().split()))
l = list(map(int, input().split()))

#初期化
dp = [float('inf')]*N
dp[0] = 0



for i in range(1,N):
    dp[i] = dp[i-1]+abs(l[i]-l[i-1])#一個前に差分を足したものに設定しておく
    for j in range(2,M+1):#２個前以降を探索
        # print(dp[i-j])どうやら,０以前の定義していないところでもinfになっているらしい
        #これはdp[-1]、つまり後ろのほうのやつが参照されているだけ
        dp[i] = min(dp[i],dp[i-j]+abs(l[i]-l[i-j]))


print(dp[N-1])
