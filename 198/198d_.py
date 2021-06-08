a = input()
b = input()
c = input()

import itertools

s = {*a,*b,*c}#文字の集合をメモする     

P = [*range(10)]

for p in itertools.permutations(P,len(set(s))):
    d = dict(zip(s,p))
    if (d[a[-1]] + d[b[-1]])%10 == d[c[-1]]:#一の位のチェック
        if len(a)>=2 and len(b)>=2 and len(c)>=2:#二桁以上だったら
            if (d[a[-2]] + d[b[-2]])%10 == d[c[-2]] or (d[a[-2]] + d[b[-2]] + 1)%10 == d[c[-2]]:#十の位のチェック
                if d[a[0]]!=0 and d[b[0]]!=0 and d[c[0]]!=0:#先頭の位が0でないかチェック
                    send = int("".join([str(d[i]) for i in a]))
                    more = int("".join([str(d[i]) for i in b]))
                    money = int("".join([str(d[i]) for i in c]))

                    if send + more == money:
                        #print(d)
                        print(send)
                        print(more)
                        exit(print(money))
        else:
            if d[a[0]]!=0 and d[b[0]]!=0 and d[c[0]]!=0:#先頭の位が0でないかチェック
                send = int("".join([str(d[i]) for i in a]))
                more = int("".join([str(d[i]) for i in b]))
                money = int("".join([str(d[i]) for i in c]))

                if send + more == money:
                    #print(d)
                    print(send)
                    print(more)
                    exit(print(money))


        
print("UNSOLVABLE")