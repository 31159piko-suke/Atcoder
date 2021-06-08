N = int(input())
s = input()

# import itertools

# s_=[]
# for i in range(N):
#     if s[i]=="E":
#         s_.append(1)
#     else:
#         s_.append(-1)
# s_accm = list(itertools.accumulate(s_))

s_accm = [0]
for i in range(N):
    if s[i]=="E":
        s_accm.append(s_accm[i]+1)
    else:
        s_accm.append(s_accm[i]-1)

l_idx = s_accm.index(max(s_accm))
E_num = sum([1 for i in s[l_idx+1:] if i=="E"])
W_num = sum([1 for i in s[:l_idx] if i=="W"])

print(E_num+W_num)
