Random Teams
"""
题目链接:
  https://codeforces.com/problemset/problem/478/B
思考：（1300分）
最大分配一定是前m-1个分1个，第m个分n - m + 1个，算第m组的最大
最小分配是，找出商和余数d 和 r，那么把r分给其他组，有r组是d + 1个人，剩余m - r组是d个人。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
n, m = map(int, input().split())
d,r = n // m, n % m
k = n - m + 1
k_max = k * (k - 1) // 2
k_min = r * (d + 1) * d // 2 + (m - r) * d *(d - 1) // 2
print(k_min, k_max)
