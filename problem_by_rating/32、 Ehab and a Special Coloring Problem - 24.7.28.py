Ehab and a Special Coloring Problem
"""
题目链接:
https://codeforces.com/problemset/problem/1174/C
思路：（1300）
有点类似于埃式筛，构造他们的倍数为自身相同的数。
"""
Python代码:
n = int(input())
a = [0] * (n + 1)
t = 1
for i in range(2, n + 1):
    if not a[i]:
        for j in range(i, n + 1, i):
            a[j] = t
        t += 1
print(*a[2:])
