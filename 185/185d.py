N,M = map(int,input().split())
l = list(map(int,input().split()))

l.sort()
if not l:#青ますがないとき
    print(1)
    exit()

if N==M:#全部青ますのとき
    print(0)
    exit()


a = []
for i in range(M-1):
    a.append(l[i+1]-l[i]-1)

if not l[0]==1:#あたまケア
    a.append(l[0]-1)

if not N==l[-1]:#しりケア
    a.append(N-l[-1])


a = list(filter(lambda x: x>0 ,a))#０を除く、つまり、連続青ます

k = min(a)



result = 0
for i in range(len(a)):
    if a[i]%k==0:
        result += a[i]//k
    else:
        result += a[i]//k+1
print(result)
