Simple Game
"""
题目链接:https://codeforces.com/contest/570/problem/B
思路：（1300）
找出m左边和右边两个区间哪边更大，只需要让a放在m旁边，且是区间最大的一侧就可。注意n = 1的情况，这时候只能选1
"""
Python代码:
n, m = map(int,input().split())
print(1 if n == 1 else m + (-1 if n - m <= m - 1 else 1))
