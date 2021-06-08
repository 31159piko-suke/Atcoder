N = int(input())
 
 
if N==1:
    exit(print(1))
 
L = []
A = []
for i in range(N):
    a = int(input())
    A.append(a)
    l = []
    for j in range(a):
        l.append(list(map(int,input().split())))
    L.append(l)
 
 
 
result = [0]
for i in range(2**N):
    bool_l = bin(i)[2:].zfill(N)#正直者とうそつきを仮定する
    flug = True
    for j in range(N):#全員に対して
        if (i>>j) & 1:#正直者なら
            for k in range(A[j]):#すべての証言があっているか
                if not flug: continue#誰かがだめならその後は無意味
                idx = -L[j][k][0]
                Bool = L[j][k][1]
 
                if int(bool_l[idx])!=Bool:
                    flug = False
 
 
    if flug:
        result.append(sum([1 for i in bool_l if i == "1"]))
 
print(max(result))