N,M = map(int,input().split())
X = [tuple(map(int,input().split())) for i in range(M)]
K = int(input())
Y = [list(map(int,input().split())) for i in range(K)]

import numpy as np
d = []
result = []

def rec(i,d):
    #全員が皿をいずれかにおいたら合格条件をカウント
    if i==K:
        count = sum([1 for j in range(M) if set(X[j]) <= set(d)])
        result.append(count)
        return 0

    #まず一つ目のテーブルを選択して再帰
    d.append(Y[i][0]) 
    rec(i+1,d)
        
    #先ほどのテーブルから皿を回収して二つ目のテーブルに置いてみて再帰
    d.pop()
    d.append(Y[i][1]) 
    rec(i+1,d)
    
    #帰ってきたら皿を回収して再帰
    d.pop()
    return 0

rec(0,d)
print(max(result))
