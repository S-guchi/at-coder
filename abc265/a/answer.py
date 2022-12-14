"""
問題文
果物屋さんでりんごが売られています。
あなたは次の操作を好きな順で好きなだけ繰り返すことができます。

X 円を払ってりんごを 1 個手に入れる。
Y 円を払ってりんごを 3 個手に入れる。
りんごをちょうど N 個手に入れるには最低何円必要ですか？

制約
1≤X≤Y≤100
1≤N≤100
入力される値はすべて整数

入力
入力は以下の形式で標準入力から与えられる。

X Y N
出力
答えを整数として出力せよ。

"""
# X, Y, N = map(int, input().split())
# if N < 3:
#     print(X * N)
# elif Y / 3 > X:
#     print(X * N)
# else:
#     cnt = N / 3
#     if N % 3 > 0:
#         print(cnt * Y)
#     else:
#         mod = N % 3
#         print((cnt * Y) + (mod * X))
# ↑解けず、、解説を見る

# pythonの除算を知らんかった
# //で整数部だけ出せる
X, Y, N = map(int, input().split())
if X * 3 > Y:
    print((N // 3) * Y + (N % 3) * X)
else:
    print(X * N)
