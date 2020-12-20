Sx,Sy,Gx,Gy = list(map(int,input().split()))

Gy = -Gy

if Gy == Sy:
    print((Gx-Sx)//2)
else:
    print(-Sy*(Gx-Sx)/(Gy-Sy)+Sx)
