N,A,B = map(int,input().split())

sum_= 0
for i in range(N+1):
    result = sum(list(map(int, str(i))))
    if A<=result and result<=B:
        sum_+= i

print(sum_)
