Permutation Operations
"""
题目链接:
https://codeforces.com/problemset/problem/1746/C
思路：（1300）
让每个数都等于n + 1即可，这样可以构造出一个递增的结果。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
#构造出相同的数
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = [0] * n
    for i in range(n):
        b[n - a[i]] = i + 1
    print(*b)

