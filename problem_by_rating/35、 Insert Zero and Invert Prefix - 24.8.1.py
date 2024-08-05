Insert Zero and Invert Prefix
"""
题目链接:https://codeforces.com/contest/1839/problem/C
思路：（1300）
相同的数一定是统一处理的，不同的数是不同处理的。
将相同处理的放一起，不同处理的放在末尾。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if a[-1] == 1:
        print("NO")
        continue
    res = [0]+[0 for i in range(1, n) if a[i - 1] == a[i]] +[i for i in range(1, n)if a[i - 1] != a[i]]
 
    print("YES")
    print(*res)
