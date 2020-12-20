import math

n = int(input())
ans = 0

for i in range(n//3):

    box = i+1

    boll = n-box*3

    a = math.factorial(box-1 + boll)//(math.factorial(box-1)*math.factorial(boll))
    ans += a
print(int(ans%(10**9+7)))
