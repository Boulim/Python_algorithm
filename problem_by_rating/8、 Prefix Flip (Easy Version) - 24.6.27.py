 Prefix Flip (Easy Version)
"""
题目链接:https://codeforces.com/problemset/problem/1381/A1
8、 Problem - 1381A1 - Codeforces
思路：（1300）
从头开始遍历，每次只改变当前a[i]和目标b[i]的不同位，需要三次操作，分别是操作第i位，
操作第1位，操作第i位，这样就完成了只对第i位的更改，a[i]和b[i]也相同了。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    a = str(input())
    b = str(input())
    ans = []
    for i in range(n):
        if a[i] != b[i]:
            ans += [i + 1, 1, i + 1]
    print(len(ans),*ans)


