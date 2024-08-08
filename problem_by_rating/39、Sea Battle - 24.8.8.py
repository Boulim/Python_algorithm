Sea Battle
"""
题目链接:https://codeforces.com/problemset/problem/729/D
思路：(1700)
将每个串按照 1 分成不同的 0 串。先计算保证打到 a 艘船的最小值，再减去 a - 1 艘船，就是最少打到 1 艘船的最小值。
对每个 0 串，当长度达到 b，便把坐标加入答案。 
最后再随机扔去 a - 1 个答案
输入该答案即可
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()

n, a, b, k = map(int, input().split())
s =  input()
ans = []
cnt = 0
for i,c in enumerate(s):
    if c == '0':
        cnt += 1
        if cnt == b:
            ans.append(i + 1)
            cnt = 0
    else:
        cnt = 0
t = len(ans) - a + 1
print(t)
print(*ans[:t])
