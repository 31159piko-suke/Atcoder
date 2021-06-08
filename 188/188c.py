N = int(input())
A = list(map(int,input().split()))
 
l_1 = sorted(A[:(len(A)//2)])
l_2 = sorted(A[(len(A)//2):])
 
print(A.index(min(l_1[-1],l_2[-1]))+1)