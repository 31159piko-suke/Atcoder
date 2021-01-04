N = int(input())
l = list(map(int,input().split()))

result = 1
if N%2==0:
    for i in range(N//2):
        result *= l[i] * l[N-1-i]
else:
    for i in range(N//2):
        result *= l[i] * l[N-1-i]
    result *= l[N//2]




if result>10**18:
    print(-1)
    exit()
print(result)