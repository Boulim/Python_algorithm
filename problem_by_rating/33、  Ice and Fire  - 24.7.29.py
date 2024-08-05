 Ice and Fire
"""
题目链接:
https://codeforces.com/contest/1774/problem/C
思路：（1300）
当前如果和前一位数字相同，那么结果是一样的。如果和前一位不同，结果就是当前位+ 1
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    s = input()
    res = [1]
    for i in range(1, n - 1):
        if s[i] != s[i - 1]:
            res.append(i + 1)
        else:
            res.append(res[-1])
    print(*res)


