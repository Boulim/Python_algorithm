Matching Numbers
"""
题目链接:
https://codeforces.com/problemset/problem/1788/C
思考：（1300）
n为偶数会有偶数对，不能凑齐答案
n为奇数，答案的每对和是以 2 * n + 1 - n // 2为开始的n - 1个数
剩下的数分别是1- n，但是要保持一对和递增，是先1，3，5。。再2，4，6。。。
所以要先枚举奇数，再枚举偶数
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        print('No')
        continue
    print("Yes")
    a = 2 * n + 1 - n // 2
    for i in range(1,n + 1,2):
        print(a - i,i)
        a += 1
    for i in range(2, n + 1, 2):
        print(a - i,i)
        a += 1
       
