Coin Rows
"""
题目链接:https://codeforces.com/contest/1555/problem/C
思路：（1300）
分别维护两个数组，分别表示左上角的数组和，右下角的数组和。先求出第一行的行和，
再遍历1-m时，开始计算第二行右下角的数组和，同时减少左上角的数组和。来表示bob能走的路的值。
返回值为两个数组各自和的最小的最大值。或者用m数组维护，每次加入两个数组和的最大值。返回m的最小值，
也就是两个数组各自和的最小的最大值。
"""
Python代码:
import sys
inout = lambda:sys.stdin.readline().strip()
from math import inf
for _ in range(int(input())):
    m = int(input())
    a = []
    for _ in range(2):
        a.append(list(map(int,input().split())))
    alice = sum(a[0])
    bob = 0
    ans = inf
    for i in range(m):
        alice -= a[0][i]
        ans = min(ans,max(alice,bob))
        bob += a[1][i]
    print(ans)

