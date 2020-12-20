N = input()

result = sum(map(int, N))
# print(result)
if result%9==0:
    print("Yes")
else:
    print("No")
