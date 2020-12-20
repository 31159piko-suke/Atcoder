N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]

count = 0
flug = 0
# print(N)
for i in range(N):
    if l[i][0]==l[i][1]:
        count += 1
    else:
        count = 0
    if count == 3:
        flug = 1
        break

if flug == 1:
    print("Yes")
else:
    print("No")
