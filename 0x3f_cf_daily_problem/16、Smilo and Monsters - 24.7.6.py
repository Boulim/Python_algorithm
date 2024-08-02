Smilo and Monsters
"""
题目链接:
   Problem - 1891C - Codeforces
思路：（1500）
用操作一操作小的数，用操作二操作大的数，可以让总操作次数尽量小。
设 s = sum(a)，left = ceil(s/2)。
把 a 从小到大排序。不断地把 left 减少 a[i]，直到 left < a[i] 为止。此时我们积累了足够的能量，剩余的 n - i 个数（i 从 0 开始）全部用操作二搞定。答案为 ceil(s/2) + n - i。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    s = sum(a)
    left = (s + 1) // 2
    ans = left
    for i,x in enumerate(a):
        if left < x:
            ans += n - i
            break
        left -= x
    print(ans)
