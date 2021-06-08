K = int(input())
S = input()

result = S if len(S)<=K else S[:K]+"..."

print(result)