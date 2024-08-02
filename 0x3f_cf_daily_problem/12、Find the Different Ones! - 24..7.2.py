Find the Different Ones!
"""
题目链接:
  Problem - D - Codeforces
思路：（1300）
定义 left[i] 表示在 a[i] 左侧的不等于 a[i] 的最近元素下标。
递推：如果 a[i] = a[i-1] 则 left[i] = left[i-1]，否则 left[i] = i-1，表示在 i 处发生了变化
回答询问时，如果 left[R] < L ，表示从L- R没有一处变化，则输出 -1 -1，否则输出 left[R] 和 R，表示发生变化的地方在L的右边， 并且发生变化的下边存储在left[r]中
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    p = [-1] * n
    for i in range(1,n):
        p[i] = p[i - 1]
        if a[i] != a[i - 1]:
            p[i] = i - 1    
    for _ in range(int(input())):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        if l > p[r]:
            print("-1 -1")
        else:
            print(p[r] + 1, r + 1)
