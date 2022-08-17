n = int(input())
p_list = [0, 0] + list(map(int, input().split()))
point = p_list[n]
t = 1
while point != 1:
    point = p_list[point]
    t += 1
print(t)
