def insuubunnkai(n):#因数分解したリストを返す関数
    b = 2
    fct = []
    while b*b<n:
        while n%b==0:
            n //= b
            fct.append(b)
        b += 1

    if n != 1:
        fct.append(n)

    return fct

n = int(input())
ans = 0
for a in range(1, n):
  ans += (n - 1) // a
print(ans)
