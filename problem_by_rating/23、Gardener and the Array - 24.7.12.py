Gardener and the Array
"""
题目链接:
https://codeforces.com/contest/1775/problem/B
思路：（1300）
# import sys
# input = sys.stdin.readline
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     li = [list(map(int, input().split())) for _ in range(n)]
#     from collections import Counter
#     c = Counter()
#     for i in range(n):
#         for j in range(1,len(li[i])):
#             c[li[i][j]] += 1
#     for i in range(n):
#         if all(c[li[i][j]] > 1 for j in range(1,len(li[i]))):
#             print("Yes")
#             break
#     else:
#         print("No")
from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    d = defaultdict(set)
    for i in range(n):
        k, *a = [*map(int, input().split())]
        for v in a:
            d[v].add(i)
    s = set()
    for v in d:
        if len(d[v]) == 1:
            s.add(d[v].pop())
    print('No' if len(s) == n else 'Yes')



