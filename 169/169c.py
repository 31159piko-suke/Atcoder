A,B = map(float,input().split())

import decimal
B = decimal.Decimal(str(B))
A = decimal.Decimal(str(A))
print(int(A*B))
