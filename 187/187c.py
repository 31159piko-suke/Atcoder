N = int(input())
l = [input() for _ in range(N)]
l_neo = [l[i][1:] if "!" in l[i] else "!"+l[i] for i in range(N)]

result = list(set(l) & set(l_neo))

if result:
    if "!" in result[0] :
        print(result[0][1:])
        exit()
    else:
        print(result[0])
        exit()
else:
    print("satisfiable")


# l.sort()

# count = 0
# for i in range(N):
#     if "!" in l[i]:
#         count += 1
#     else:
#         break

# l_1 = l[:count]
# l = l[count:]
# # print(l_1)
# # print(l)
# for i in range(len(l_1)):
#     if l_1[i][1:] in l:
#         print(l_1[i][1:])
#         exit()

# for i in range(len(l)):
#     if l[i][1:] in l_1:
#         print(l[i])
#         exit()

# print("satisfiable")