Fill in the Matrix
"""
题目链接:
https://codeforces.com/contest/1868/problem/A
思路：（1300）
分类讨论
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(min(m, n + 1) if m > 1 else 0)
    a = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            a[i][j] = (min(i, m - 2) + j + 1) % m
        print(*a[i])
