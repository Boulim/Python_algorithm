Array Painting
"""
题目链接:
  Problem - 1849D - Codeforces
思路：（1700）
看当前的数，能否通过左右的数变成红色。
强制a[i] = 0，这样a[i+1]不能用a[i]更新，不会出现a[i]使用a[i+1]更新，a[i+1]使用a[i]更新的情况
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
n = int(input())
a = [0] + list(map(int,input().split())) + [0]
cnt = 0
for i in range(1,n + 1):
    if a[i - 1]:
        a[i - 1] -= 1
    elif a[i] == 0 and a[i + 1]:
        a[i + 1] -= 1
    else:
        cnt += 1  
print(cnt)

