R,X,Y = map(int,input().split())

k = (X**2+Y**2)**0.5
R = R

if k<R:
    exit(print(2))
if k==R:
    exit(print(1))

count = 0
while True:
    if k-R>0:
        k = k-R
        count += 1
    else:
        break
print(count)