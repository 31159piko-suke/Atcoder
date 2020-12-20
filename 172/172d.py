N = int(input())



table=[0]*(N+1)
for i in range(1,N+1):
    for j in range(i,N+1,i):
        table[j]+=1
ans=0
for i in range(1,N+1):
    ans+=i*table[i]



print(ans)
