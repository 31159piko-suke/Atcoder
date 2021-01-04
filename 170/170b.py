X,Y = map(int,input().split())

#ｎ鶴の数、mカメの数

m = (Y-2*X)/2
n = X-m


if m%1==0 and n%1==0 and m*n>=0:
    print("Yes")
    
else:
    print("No")
