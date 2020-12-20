N = int(input())
l = list(map(int,input().split()))

import math

#累積和関数
def cumsum(xs):
  result = [xs[0]]
  for x in xs[1:]:
    result.append(result[-1] + x)
  return result

m = []
y = []
c = []
for i in range(N):
    m.append(abs(l[i]))
    y.append(l[i]**2)
    c.append(abs(l[i]))

print(sum(m))
print(math.sqrt(sum(y)))
print(max(c))
