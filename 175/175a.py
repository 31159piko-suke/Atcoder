L = input()

max_ = 0
max_list = []
for i in L:
    if i=="R":
        max_ += 1
        max_list.append(max_)
    else:
        max_ = 0

if not max_list:
    print(0)
else:
    print(max(max_list))
