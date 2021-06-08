N = input()
N = list(N)
for i in range(1,len(N)):
    if N[-1]=="0":
        N.pop()
    else:
        break

for i in range(len(N)//2):
    if N[i]==N[-(i+1)]:
        pass
    else:
        exit(print("No"))
print("Yes")