N,M,T = map(int,input().split())
import itertools

l = []
for i in range(M):
    l.append(list(map(int,input().split())))
l = list(itertools.chain.from_iterable(l))
l.append(T)

left = N-l[0]
flug = 0
if left==0:
  print("No")
  exit()
for i in range(0,2*M):

    if flug%2==0:
        left += l[i+1]-l[i]
        if left>=N:
            left = N
        flug += 1
    else:
        left -= l[i+1]-l[i]
        flug += 1

    if left <= 0:
        print("No")
        exit()

print("Yes")
