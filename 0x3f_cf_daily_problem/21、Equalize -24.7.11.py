Equalize
"""
题目链接:  
  Problem - C - Codeforces
思路：（1300）

如果是相邻两个，就让他换。如果不是相邻，最佳选择是直接更改
"""
Python代码：
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

