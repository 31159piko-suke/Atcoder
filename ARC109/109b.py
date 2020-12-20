n = int(input())
import math
import decimal

# bisect.bisect_left(A, 3)

x = decimal.Decimal('0.5')

result = math.floor(((-1+(1+8*(n+1))**x)/2))-1

print(n-result)
