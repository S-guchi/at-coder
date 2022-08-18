# チェス版距離
# max(abs(R-8),abs(C-8))の結果が奇数ならblack、偶数ならwhite
R, C = map(int, input().split())

if max(abs(R - 8), abs(C - 8)) % 2:
    print("black")
else:
    print("white")
