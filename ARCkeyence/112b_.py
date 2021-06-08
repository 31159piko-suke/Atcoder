N,K =  map(int,input().split())
A = list(map(int,input().split()))

if not 0 in A:#0がないとき0
  exit(print(0))
  
import collections

c = collections.Counter(A)
c = sorted(c.items())

for i in range(len(c)):#list化
    c[i] = list(c[i])

for i in range(len(c)-1):#連続部分だけとる
    if c[i+1][0]-c[i][0]>=2:
      c = c[:i+1]
      break

result =0
for _ in range(K):#一箱ずつ考える
    flug = 0
    for j in range(len(c)):
        if c[j][1]<=0:
            result += j
            flug = 1
            break
       
        c[j][1] -= 1#玉を入れる
        
    if not flug:#全部一個ずつあったら
        result += j+1
        
print(result)