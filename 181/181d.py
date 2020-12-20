from collections import Counter

n = input()
len_n = len(n)

if len(n) <= 2:
    if int(n)%8==0 or int(n[::-1])%8 == 0:
        print("Yes")
    else:
        print("No")
    exit()

else:
    cnt = Counter(n)
    for i in range(104,1000,8):
        c = Counter(str(i)) - cnt
        if not c:
            print("Yes")
            exit()
print("No")
