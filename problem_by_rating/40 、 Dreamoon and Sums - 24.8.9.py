Dreamoon and Sums
"""
题目链接:https://codeforces.com/problemset/problem/476/C
思路：（1600）
先推理k， k可以是1 - a, 等差数列求和搞
再推理x mod b 为多少，x mod b 可以为 1 - b - 1. 当mod为 0，则不存在. 可以等差数列搞
整合出一个数学公式 O(1)拿下ac

"""
Python代码:
mod = 10 ** 9 + 7
a, b = map(int, input().split())
p = (b - 1) * b // 2
q = a * (a + 1) // 2
ans = (p * q * b + a * p) % mod
print(ans)
