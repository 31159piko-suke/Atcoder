S = input()
T = input()

max_ = 0
for i in range(len(S)-len(T)+1):
    count=0
    for j in range(len(T)):
        if S[i+j]==T[j]:
            count += 1
    if count>max_:
        max_ = count

print(len(T)-max_)
