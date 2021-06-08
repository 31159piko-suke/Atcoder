N,M = map(int,input().split())
l = [list(map(int, input().split())) for _ in range(M)]

l_neo = set()
for i in l:
    l_neo.add((min(i[0],i[1]),max(i[0],i[1])))
l_neo = sorted(l_neo)

print(l_neo)