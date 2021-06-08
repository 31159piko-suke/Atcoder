N = int(input())
B = list(map(int,input().split()))


result = sum([min(B[i],B[i+1]) for i in range(N-2)]) + B[0] + B[-1]
print(result)