"""
N  個の正の整数 a0,a1,…,aN−1 と、正の整数 W とが与えられます。

a0,a1,…,aN−1 の中から何個か選んで総和を W とすることができるかどうかを判定してください。
"""
def rec(n,sum):
    if n==len(a):
        return True if sum==W else False
    
    if rec(n+1,sum+a[n]): return True

    if rec(n+1,sum): return True

    return False

a = [1,2,3,4,5,6,7,8,9,10]
W = 56
result = rec(0,0)
print(result)
