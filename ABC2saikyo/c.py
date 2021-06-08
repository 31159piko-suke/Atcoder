A ,B = map(int,input().split())

import itertools
import math
import collections

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


l = [*range(A,B+1)]


a = []
b = {}
for i in l:
    a.append(make_divisors(i))
   
L = sum(a,[])
c = collections.Counter(L)


for i,k in c.items():
  if (i <= B-A) and k>=2:
    b.update({i:k})
    
  
print(max(b))