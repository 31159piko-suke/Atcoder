N = int(input())
T = input()
# if ('111' or '00' or '010') in T:
#     print(0)
#     exit()

s = "110" * (10**5)
if not T in s:
    print(0)
    exit()


if T=='1':
    print(2*10**10)
    exit()

count = T.count('0')

if T[-1]=='1':
    print(10**10-count)
else :
    print(10**10-count+1)




