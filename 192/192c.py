N,K = map(int,input().split())

if K == 0:
    print(N)
    exit() 

N = str(N)
N_list = list(N)

for _ in range(K):
    g_1 = sorted(N_list)[::-1]
    g_2 = sorted(N_list)

    g_1 = int(''.join(g_1))
    g_2 = int(''.join(g_2))

    f = g_1-g_2
    f_str  = str(f)
    N_list = list(f_str)
print(f)