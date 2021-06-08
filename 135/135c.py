N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

count = 0
for i in  list(range(N))[::-1]:
    if min(A[i+1],B[i])==A[i+1]:
        count += A[i+1]
        B[i] -= A[i+1]
        A[i+1] = 0
        
    else:
        count += B[i]
        A[i+1] -= B[i]
        B[i] = 0

    if min(A[i],B[i])==A[i]:
        count += A[i]
        B[i] -= A[i]
        A[i] = 0
        
    else:
        count += B[i]
        A[i] -= B[i]
        B[i] = 0

print(count)