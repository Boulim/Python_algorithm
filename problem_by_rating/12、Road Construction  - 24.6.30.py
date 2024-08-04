Road Construction
"""
题目链接:https://codeforces.com/problemset/problem/330/B
思考：（1300）
由于限制边数m小于n/2，当m=n/2时，最坏情况是两个城市之前有一个限制路，
也就是m条边分别连接n个点。完全匹配。由于m小于n/2，所以一定有一个点没有被任何一条路限制。
只需让其他城市都与这个城市建立直接地连接就好。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
n,m = map(int,input().split())
c = [0] * n
for _ in range(m):
    a,b = map(int, input().split())
    c[a - 1] += 1
    c[b - 1] += 1
t = 0
for i in range(n):
    if c[i] == 0:
        t = i
        break
print(n - 1)
for i in range(n):
    if i != t:
        print(i + 1,t + 1)

