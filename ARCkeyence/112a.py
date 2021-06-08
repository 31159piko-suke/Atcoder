N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

max_ = 0
for i in range(N):
    if A[i]>max_:
        max_ = A[i]
    else:
        A[i] = max_

m = A[0]*B[0]
print(m)
for i in range(1,N):
    if m<A[i]*B[i]:
        m = A[i]*B[i]
    print(m)

