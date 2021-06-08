import math
X,Y,R = map(float,input().split())
X,Y,R = 10000*X,10000*Y,10000*R
min_y = math.ceil(Y-R)
max_y = math.floor(Y+R)
min_y = 10000*min_y
max_y = 10000*max_y
 
count = 0
for y in range(min_y,max_y+1):
    min_x = math.ceil(-(R**2-(y-Y)**2)**0.5+X)
    max_x = math.floor((R**2-(y-Y)**2)**0.5+X)
    count += max_x - min_x + 1
print(count/100000000)