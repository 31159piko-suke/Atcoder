A,B,C = map(int,input().split())


if A-B!=0:
    print("Takahashi" if A>B else "Aoki")


else:
    if C==0:
        print("Aoki")
    if C==1:
        print("Takahashi")

