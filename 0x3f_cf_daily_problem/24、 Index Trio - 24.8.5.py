Index Trio
"""
题目链接:https://atcoder.jp/contests/abc249/tasks/abc249_d
思路：
用Counter统计每个数的次数。在这之前记录数组的最大值。
枚举 i 和 j，根据乘法原理，有 cnt[i]*cnt[j]*cnt[i*j] 个三元组是满足要求的，加到答案中。
二重循环减少时间复杂度，就用调和级数。
时间复杂度 O(U/1+U/2+U/3+...+U/U) = O(UlogU)，其中 U=max(a)=2e5。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
from collections import Counter

n = int(input())
a = list(map(int, input().split()))
cnt = Counter(a)
ma = max(a)
ans = 0
for i in range(1, ma + 1):
    for j in range(1, ma // i + 1):
        ans += cnt[i] * cnt[j] * cnt[i * j]
print(ans)
