# N = int(input())
# A = list(map(int,input().split()))
#
# import numpy as np
# A.sort()
#
# table = np.ones(max(A))
# for i in range(N):
#     for j in range(2,max(A)//A[i]+1):
#         table[A[i]*j] -= 1
#
#
#
#
# print(np.count_nonzero(table[A]==1))




#https://note.com/tanon_cp/n/nac7cd1eb1361
import collections

n=int(input())
arr=list(map(int,input().split()))
arr=sorted(arr) #小さい順にソートしておく
s=set()
cnt=collections.Counter(arr) #各要素の個数を事前に数えておく
for i in range(n):
    if arr[i] in s: #Aiがすでに列挙した数に含まれていれば処理を行わない
        continue
    if cnt[arr[i]]>=2: #Aiが2個以上含まれているとき、Ai自身を列挙した数に加える
        s.add(arr[i])
    for j in range(2,10**6//arr[i]+1): #Ai自身を除くAiの倍数を列挙する
        s.add(arr[i]*j)
ans=0
for i in range(n): #列挙した数に含まれないAiの個数を数える
    if arr[i] in s:
        continue
    ans+=1
print(ans)
