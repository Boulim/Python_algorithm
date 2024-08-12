Similar Arrays
"""
题目链接:https://codeforces.com/contest/1090/problem/D

思路：（1800）
将数组建立成一个图，如果是一个完全图，不能找出答案。

如果不是完全图，找出缺少的边，让其两个端点分别为 1 和 2 ，再补充其他位置的数， 打印输出原数组

再将第二个端点变为 1 ，打印输出变化后的数组
"""
#Python代码：
n, m = map(int, input().split())
edges = set()
for i in range(m):
    x,y = map(int, input().split())
    edges.add((min(x, y), max(x, y)))

if m == n * (n - 1) // 2:
    print('NO')
    exit()

edge = None
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if (i, j) not in edges:
            edge = (i - 1, j - 1)
            break
    if edge:
        break
print('YES')
x, y = edge
res = [0] * n
res[x] = 1
res[y] = 2
cur = 3
for i in range(n):
    if res[i] == 0:
        res[i] = cur
        cur += 1
print(*res)
res[y] = 1
print(*res)
