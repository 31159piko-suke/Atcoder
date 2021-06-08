N,X = map(int,input().split())
A = list(map(int,input().split()))

l = [i for i in A if i != X]
print(*l)