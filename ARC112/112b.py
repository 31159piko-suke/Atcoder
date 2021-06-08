B,C = map(int,input().split())
 
    
if B>0:
    if C == 0:
        print(1)
        exit()
    elif C == 1:
        print(2)
        exit()
 
    result_1 = (2*C-1)
    result_2 = (2*2*B-1) + (C-(2*B))
    
    if C<=2*B:
        print(result_1)
    else:
        print(result_2)


elif B<0:
    B = abs(B)
    if C == 0:
        print(1)
        exit()
    elif C == 1:
        print(2)
        exit()
 
    result_1 = (2*C-1)
    result_2 = 2*(2*B+1)-1 + (C-(2*B+1))

    if C<=2*B+1:
        print(result_1)
    else:
        print(result_2)

else:
    if C<2: 
        print(1)
        exit()
    else:
        print(C)
        exit()