N = int(input())

L = []
A = []
for i in range(N):
    a = int(input())
    A.append(a)
    l = []
    for j in range(a):
        l.append(list(map(int,input().split())))
    L.append(l)


result = 0
for i in range(2**N):
    flug = True
    for j in range(N):#全員に対して
        if (i>>j) & 1:#正直者なら
            for x,y in L[j]:#すべての証言があっているか
                if not flug: continue#誰かがだめならその後は無意味
                if (i>>(x-1))&1 != y:#仮定したx人目の属性と、証言yが合っているかいないか
                    flug = False
                
    if flug:
        result = max(result,(sum([1 for i in bin(i)[2:] if i == "1"])))

print(result)