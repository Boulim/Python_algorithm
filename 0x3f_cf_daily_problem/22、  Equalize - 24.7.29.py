Equalize
"""
题目链接：
https://codeforces.com/contest/1037/problem/C
思路：（1300）
为了使代价最小，我们只应在有两个连续位置(且值相反)需要固定时使用交换操作。
对于其他需要固定的位置，我们可以使用翻转操作。
"""

Python代码:
n = int(input())
a = input()
b = input()
s = i = 0
while i < n:
    if a[i] != b[i]:
        if i < n - 1 and a[i] == b[i + 1] and a[i + 1] == b[i]:
            i += 1
        s += 1
    i += 1
print(s)
