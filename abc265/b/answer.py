"""
https://atcoder.jp/contests/abc265/tasks/abc265_b
繰り返し処理でA1,A2,A3を持ち時間から引いていき文字時間がマイナスになった時点で
何番目の部屋に行けたかを調べる
ボーナス部屋の秒数は随時足す

"""
# N, M, T = map(int, input().split())
# a_list = [0]+list(map(int, input().split()))
# xy = [map(int, input().split()) for _ in range(M)]
# x, y = [list(i) for i in zip(*xy)]


# room = 1
# while T > 0:
#     T = T - a_list[room - 1]
#     if T <= 0:
#         break
#     room += 1

#     if room in x:
#         T = T + y[x.index(room)]

#     if room + 1 >= M:
#         break

# if room > M:
#     print("Yes")
# else:
#     print("No")

# 解説みた
N, M, T = map(int, input().split())
A = [0] + list(map(int, input().split()))
bonus = [0] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    bonus[x] = y
# i -> i+1
for i in range(1, N):
    if T <= A[i]:
        print("No")
        exit()
    T -= A[i]
    T += bonus[i + 1]
