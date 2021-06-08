"""
N  個の正の整数 a0,a1,…,aN−1 と、正の整数 W とが与えられます。

a0,a1,…,aN−1 の中から何個か選んで総和を W とすることができるかどうかを判定してください。
"""
def rec(n,w):
    if n==len(a):
        return True if w==0 else False
    
    if rec(n+1,w-a[n]): return True

    if rec(n+1,w): return True

    return False

a = [1,2,3,4,5,6,7,8,9,10]
W = 2
result = rec(0,W)
print(result)