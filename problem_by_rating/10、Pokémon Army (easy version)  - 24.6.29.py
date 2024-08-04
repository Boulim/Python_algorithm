Pokémon Army (easy version)
"""
题目链接:
https://codeforces.com/problemset/problem/1420/C1
思路：（1300）
计算每段连续上升序列的最大值减去最小值。结果就是答案。
从最小开始，递增时每次加上两项差值，这样到第一个递减时，前一段结果就是前边元素最大值减去前边元素最小值。
再将结果与当前元素取一个max。
"""
Python代码1:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    s = a[0]
    for i in range(1,n):
        if a[i] > a[i - 1]:
            s += a[i] - a[i- 1]
        s = max(s,a[i])
    print(s)
"""
方法2，用d1表示子序列为奇数长度，可以由自身奇数长度不选，或者偶数长度选一个，即加一个得到
。d2表示子序列为偶数长度，可以不选，或者由奇数长度子序列减去一个得到。
两者都取max，结果就是奇序列和偶数列两者的最大值
"""
Python代码2:
import sys
input = lambda:sys.stdin.readline().strip()
def max(a,b):
    return a if a > b else b
for _ in range(int(input())):
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    d1 = d2 = 0
    for x in a:
        d1 = max(d1, d2 + x)
        d2 = max(d2, d1 - x)
    print(max(d1, d2))

