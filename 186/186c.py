N = int(input())

s = set()
for i in range(1,N+1):
    ten = str(i)
    eight = oct(i)
    if "7" in ten:
        s.add(i)
    if "7" in eight:
        s.add(i)

print(N-len(s))
