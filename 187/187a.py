A,B = map(str,input().split())

A = sum(map(int, A))
B = sum(map(int, B))

if A>B:
    result = A
else:
    result = B

print(result)