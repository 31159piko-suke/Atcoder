A,B,H,M = map(int,input().split())
import math

pi = math.pi
print((A**2+B**2-2*A*B*math.cos((H/6-11*M/360)*pi))**0.5)