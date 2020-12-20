x,y,a,b = map(int,input().split())

import numpy as np


dp = np.zeros(())
#動的計画法ができない




ans=0
while a*x<=x+b and a*x<y:
  x*=a
  ans+=1

print(ans+(y-1-x)//b)
