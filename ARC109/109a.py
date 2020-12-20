a,b,x,y = map(int,input().split())

if a>b:
    if 2*x>=y:
        print(x+(abs(b-a)-1)*y)
    else:
        print(x+(abs(b-a)-1)*2*x)


else:
    if 2*x>=y:
        print(x+(abs(b-a))*y)
    else:
        print(x+(abs(b-a))*2*x)
