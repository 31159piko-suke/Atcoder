a,b = map(int,input().split())
c,d = map(int,input().split())

import math


X = c-a
Y = d-b
d1 = abs(X+Y)/math.sqrt(2)
d2 = abs(X-Y)/math.sqrt(2)

if X==0 and Y==0:
    print(0)
    exit()

if a+b==c+d or a-b==c-d or abs(a-c)+abs(b-d)<=3:
    print(1)
    exit()

if d1<=(3/math.sqrt(2)) or d2<=(3/math.sqrt(2)):
    print(2)
    exit()


if (X+Y)%2==0:
    if a+b==c+d or a-b==c-d:
        print(1)
    else:
        print(2)
else:
    a += 1
    if a+b==c+d or a-b==c-d:
        print(2)
    else:
        print(3)
