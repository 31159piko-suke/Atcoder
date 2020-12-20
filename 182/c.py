N = input()
import collections

number = 0

sum = 0
for i in range(len(N)):
    sum += int(N[i])


if sum%3==0:
    print(number)
else:
    c = collections.Counter(N)
    if sum%3==1:
        if c["1"] + c["4"] + c["7"]>=1:
            if len(N)<2:
                print(-1)
            else:
                number += 1
                print(number)

        elif c["2"] + c["5"] + c["8"]>=2:
            if len(N)<3:
                print(-1)
            else:
                number += 2
                print(number)

        else:
            print(-1)
    else:
        if c["2"] + c["5"] + c["8"]>=1:
            if len(N)<2:
                print(-1)
            else:
                number += 1
                print(number)

        elif c["1"] + c["4"] + c["7"]>=2:
            if len(N)<3:
                print(-1)
            else:
                number += 2
                print(number)

        else:
            print(-1)
       
