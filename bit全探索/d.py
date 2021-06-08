"""
N  個の正の整数 a0,a1,…,aN−1 と、正の整数 W とが与えられます。

a0,a1,…,aN−1 の中から何個か選んで総和を W とすることができるかどうかを判定してください。
"""
def rec(n,w):
    print(n,w)
    if d[n][w] != -1: return d[n][w]

    if n==0:
        # return True if w==0 else False
        if w==0:
            d[n][w]=1
            return d[n][w]
        else:
            d[n][w]=0
            return d[n][w]

    
    res = 0
    if w-a[n-1]>=0 and rec(n-1,w-a[n-1])==1: res=1

    if rec(n-1,w)==1: res=1
    
    d[n][w]=res

    return d[n][w]


import numpy as np 

a = [3,5,2,5,4]
W = 7
N = len(a)

d = np.full((N+1, W+1), -1)
result = rec(N,W)
print(d)
print("True" if result else "False")