T = int(input())

seki = []
for i in range(T):
    N,S,K = map(int,input().split())
    j=1
    while True:
        seki.append((j*K+S)%N)
        if j*K+S%N==0:
            print(j)
            break
        if j*K+S%N in seki:
            print(-1)
            break
        j+=1
