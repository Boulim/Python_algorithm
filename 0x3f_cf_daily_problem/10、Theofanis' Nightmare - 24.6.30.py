Theofanis' Nightmare
"""
题目链接:
  Problem - C - Codeforces
思路：（1400）
等价转换。和式可以视作 a 的若干后缀和之和。例如 [1,2,3,4] 分成两段 [1,2] 和 [3,4]，得分为 
(1+2)*1 + (3+4)*2= (1+2+3+4) + (3+4)
所以计算 a 的所有后缀和，取其中大于 0 的后缀和相加，即为答案。注意整个数组的和一定要加进答案。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    t, sum = 0, 0
    for i in range(n - 1, 0, -1):
        t += a[i]
        if t > 0:
            sum += t
    sum += t + a[0]
    print(sum)


