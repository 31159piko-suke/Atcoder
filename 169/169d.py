def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    
    return a


import collections
N = int(input())

c = collections.Counter(prime_factorize(N))

count = 0
for i in c.keys():
    count += (-1+(1+8*c[i])**0.5)//2

print(int(count))
# print(c)
# print(len(prime_factorize(N)))
# print(prime_factorize(N))
