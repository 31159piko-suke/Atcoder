N,K =  map(int,input().split())
A = list(map(int,input().split()))
 
import collections
import numpy as np
c = collections.Counter(A)
 
c_list = []
c_key_list = sorted(list(c.keys()))
#print(c_key_list)
 
dame = len(c_key_list)
for i in range(1,len(c_key_list)):
    if c_key_list[i]-c_key_list[i-1]>=2:
        dame = i
        break
 
#print(c_key_list)
 
for i in range(len(c_key_list)):
    c_list.append(c[c_key_list[i]])
    
    
c_list = np.array(c_list)[:dame]
#print(c_list)
    
result = 0
flug = 0
for i in range(K):
    flug = 0
    for j in range(len(list(c_list))):
        if c_list[j]<=0 and flug==0:
            result += j
            flug += 1
            break
    if flug==0:
      result += dame
 
        
 
    c_list = c_list -1
 
print(result)