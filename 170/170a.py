l = list(map(int,input().split()))
import numpy as np
l = np.array(l)
print(int(np.where(l < 1)[0])+1)
