list = input().split()

d = {}
for s in list:

    if s in d:
        d[s] += 1
    else:
        d[s] = 1

flg = False
for v in d.values():

    if v == 3 or v == 2:
        continue

    flg = True
    print("No")
    break

if flg is False:
    print("Yes")
