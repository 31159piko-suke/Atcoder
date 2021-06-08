A,B = map(int,input().split())

if A+B>=15 and B>=8:
    exit(print(1))
elif A+B>=10 and B>=3:
    exit(print(2))
elif A+B>=3:
    exit(print(3))

print(4)