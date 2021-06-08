a = input()
b = input()
c = input()

import itertools

s = {*a,*b,*c}        

P = range(10)
Q = range(1,10)

for q in itertools.permutations(Q,3):
    a1,b1,c1 = q
    if b1+c1!=a1 and b1+c1+1!=a1: continue
    R = list(set(P)-set(q))#残りの数字
    for p in itertools.permutations(R,len(set(s)-set([a[0],b[0],c[0]]))):
    
        d = dict(zip(list(set(s)-set([a[0],b[0],c[0]])), p))
        if (d[a[-1]]+d[b[-1]])%10 != d[c[-1]]: continue

        A = []
        for i in a:
            if i==a[0]:
                A.append(str(a1))
            else:
                A.append(str(d[i]))
        A = int("".join(A))
        B = []
        for i in b:
            if i==b[0]:
                B.append(str(b1))
            else:
                B.append(str(d[i]))
        B = int("".join(B))
        C = []
        for i in c:
            if i==c[0]:
                C.append(str(c1))
            else:
                C.append(str(d[i])) 
        C = int("".join(C))      

        if A+B==C:
            print(A)
            print(B)
            print(C)
            exit()

print("UNSOLVABLE")