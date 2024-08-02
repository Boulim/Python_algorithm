Where is the Pizza?
"""
题目链接:
13、 Problem - 1670C - Codeforces
思路：（1400）
用并查集将a与b连接起来，如果ab各个能连接成圈，则该区域可以构造出两个答案。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
M = 1000000007
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    p = [i for i in range(n + 1)]
    def find(x):
        if x != p[x]: p[x] = find(p[x])
        return p[x]
    ans = 1
    for i in range(n):
        if c[i] == 0 and a[i] != b[i]:#把相同的跳过，把c不为0的也跳过，建图
            pa = find(a[i])
            pb = find(b[i])
            if pa == pb:
                ans = ans*2 % M
            else:
                p[pa] = pb
    print(ans)

