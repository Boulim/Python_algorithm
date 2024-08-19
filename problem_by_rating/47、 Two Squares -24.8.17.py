"""
题目链接：https://codeforces.com/contest/993/problem/A

思路：判断一个菱形的点是否在正方形内很方便， 这样可以判断菱形是否在正方形内。

当判断正方形是否在菱形内， 可以把正方形和菱形的坐标系同时变化， 将菱形变为正方形， 此时正方形也变成了菱形。

这样就可以用一个函数来直接判断

"""
# python代码：
def check(p1, p2):
    #分别取出两个对角的值
    x1, y1 = p1[:2]
    x3, y3 = p1[4:6]
    left, right = min(x1, x3), max(x1, x3)
    down, top = min(y1, y3), max(y1, y3)
    for i in range(0, 8, 2):
        if left <= p2[i] <= right and down <= p2[i + 1] <= top:
            return True
    if left * 2 <= p2[0] + p2[4] <= right * 2 and down * 2 <= p2[1] + p2[5] <= top * 2:
        return True
    return False

def swap(x, y):
    return x + y, x - y

s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
# 判断是否相交
if check(s1, s2):
    print("YES")
    exit()
for i in range(0, 8, 2):
    s2[i], s2[i + 1] = swap(s2[i], s2[i + 1])
    s1[i], s1[i + 1] = swap(s1[i], s1[i + 1])
if check(s2, s1):
    print("YES")
else:
    print("NO")
