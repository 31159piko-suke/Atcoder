N = int(input())
A = list(map(int,input().split()))

import numpy as np

B = sorted(list(set(A)))
A = np.array(A)

max_ = N
flug = 0


for j in B:
    A -= j#もとのテーブルから引く
    count = j#縦の長さ
    
    for i in range(N):#全テーブルを順にみていく
        if A[i]==0 and flug==0:
            index = i
            flug = 1#左端をみつけたらフラグを立てる
            
        elif A[i]<0 and flug==1:
            result = count*(i-index)#縦×横
            flug = 0#右端をみつけたらフラグを下す
            if result>max_ :
                max_ = result
    if flug==1:#最後まで続いていたら最後まで食べられる
      result = count*(i-index+1)
      flug = 0
      if result>max_ :
                max_ = result
    
    A += j#与えられた入力の状態に戻す
    
    
print(max_)