N = int(input())
l = list(map(int,input().split()))
# print(l)

max = 0
result = 0

for i in l:
    if i>max:
        max = i
    else:
        result += (max-i)

print(result)
