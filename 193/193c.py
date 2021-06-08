N = int(input())

def manzi(N):
    table=[0]*(N+1)
    for i in range(1,N+1):
        for j in range(i,N+1,i):
            table[j]+=1
    return table

l = manzi(int(N**0.5))
ind_list = [i for i in range(len(l)) if l[i]<=2][2:]
print(ind_list)

t = [0]*int(N**(0.5))


for i in ind_list:
    j = 2
    flug = True
    while flug:
        if i**j<=N:
            t[i**j]+=1
            j += 1
        else :
            flug = False
print(t.count(0))