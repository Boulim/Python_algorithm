Arrow Path
"""
题目链接:https://codeforces.com/contest/1948/problem/C
思路：（1300）
只要有奇数位都为<，那么必定走不到。即走第一步的时候，都遇到了<，那么必定走不到。
分两种情况，第一种是第一步向下遇到<和向右走遇到<。（对应第一排右边可以走/）
		    第二种是向下走之后可以走，但是向上走和向右走的第一步都遇到了<（对应第二排右边可以走\）
"""		
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    s1 = input()
    s2 = input()
    for i in range(1,n,2):
        if s1[i] == s2[i - 1] == '<' or i + 1 < n - 1 and s1[i] == s2[i + 1] == '<':
            print("NO")
            break
    else:
        print("YES")

