Closest Cities
"""
题目链接:
  Problem - C - Codeforces
思路：（1300）
前缀和。
定义 R[i] 表示从 1 到 i 的花费，则有R[i+1] = R[i] + (a[i]-a[i-1] < a[i+1]-a[i] ? a[i+1]-a[i] : 1)
初始值 R[2] = 1。同理可得 L[i]，表示从 i 到 1 的花费。

对于每个询问，如果 x < y 则用 R 计算，否则用 L 计算。代码下标从 0 开始。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    #设置左右两个数组，分别代表向左走和向右走的代价,同时用前缀和处理
    l = [0] * n
    r = [0] * n
    r[1] = 1
    for i in range(1, n-1):
        if a[i] - a[i-1] < a[i+1] - a[i]:
            l[i] = l[i-1] + 1
            r[i+1] = r[i] + a[i+1] - a[i]
        else:
            l[i] = l[i-1] + a[i] - a[i-1]
            r[i+1] = r[i] + 1
    l[n-1] = l[n-2] + 1
    for _ in range(int(input())):
        x, y = map(int,input().split())
        x -= 1
        y -= 1
        if x < y:
            print(r[y] - r[x])
        else:
            print(l[x] - l[y]) 




