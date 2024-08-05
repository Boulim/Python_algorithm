Binary String Constructing
"""
题目链接:
https://codeforces.com/contest/1003/problem/B
"""
Python代码:
a, b, x = map(int, input().split())
c = ['0', '1']
if a < b:
    a, b = b, a
    c = ['1', '0']
s = c[0] * (a - x // 2) + c[1] * (b - (x - 1) // 2)
for i in range(x - 1):
    s += c[i & 1]
print(s)
