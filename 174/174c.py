N = int(input())

num = 7

for i in range(1,N+1):
    mod = num%N
    if mod == 0:
        print(i)
        exit()
    else:
        num = mod*10+7
print(-1)
