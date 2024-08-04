Nastia and a Good Array
"""
题目链接:
https://codeforces.com/contest/1521/problem/B
7、 Problem - B - Codeforces
思路：（1300）
需要让两个相邻的数最大公约数为1，替换的时候找两个数，其中一个为数组最小值位置pos，
让另一个数替换成 x + | pos - i |，数组就变成了如6543456.这种模式。
"""
Python代码1:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    x = min(a)
    j = a.index(x)
    k = 0
    print(n - 1)
    for i in range(n):
        if i == j:
            continue
        print(j + 1 ,i + 1 ,a[j],a[j] + abs(i - j))
"""
也可找一个1e7 + 9的值，让每两个数，第一个数替换成原先两数最小值，第二个变成1e7+9,这样时间复杂度变为n/2
"""
Python代码2:
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    print(n//2)
    l = 1000000007
    for i in range(0,n-1,2):
        print(i+1,i+2,min(a[i],a[i+1]),l)



