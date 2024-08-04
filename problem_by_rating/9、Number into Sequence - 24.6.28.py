Number into Sequence
"""
题目链接:https://codeforces.com/problemset/problem/1454/D
9、 Problem - 1454D - Codeforces
思路：（1300）
将n按照质数分解，分别求出来每个质数的最高次项。最高次项就是答案k，
质数就是前k-1个答案，剩下就是第k个答案，除以k-1个最高次项的质数后的余数
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    m = n
    k = 1
    p = 1
    for i in range(2,int(n**0.5) + 1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n //= i
        if cnt > k:
            k = cnt
            p = i
    print(k)
    for i in range(k - 1):
        m //= p
        print(p,end = ' ')
    print(m)

