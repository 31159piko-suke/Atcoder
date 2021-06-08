T = int(input())

for i in range(T):
    L,R = map(int,input().split())


    if R==L:
        if R==0:
            print(1)
        else:
            print(0)
    elif R-2*L+1<=0:
        print(0)
    else:
        print((R-2*L+1)*(R-2*L+2)//2)
