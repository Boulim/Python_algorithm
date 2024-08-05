Sets and Union
"""
题目链接:https://codeforces.com/problemset/problem/1882/B
思路：（1300）
把每个数组去重后装入list中(去掉第一个长度)，遍历list，用set求最终集合S，其中 | 是集合的并运算。
遍历S的每一个值，分别求不含该值的多个集合的长度。动态更新长度最大值。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for t in range(int(input())):
    n = int(input())
    tmp = [] 
    s = set()
    for _ in range(n):
        a = set(list(map(int, input().split()))[1:])
        tmp.append(a)
        s |= a
    ans = -1
    for x in s:
        b = set()
        for t in tmp:
            if x not in t:
                b |= t
        ans = max(ans, len(b))
    print(ans)


