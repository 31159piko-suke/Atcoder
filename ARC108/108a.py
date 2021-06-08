S,P = map(int,input().split())

M = (-S+(S**2-4*P)**0.5)/2
N = S-M
if M%1==0 and M*N>0:
    exit(print("Yes"))
print("No")
    