S = input()

for i in range(len(S)):
    if i%2==0:
        if S[i].islower():
            pass
        else:
            exit(print("No"))
    else:
        if S[i].isupper():
            pass
        else:
            exit(print("No"))
print("Yes")