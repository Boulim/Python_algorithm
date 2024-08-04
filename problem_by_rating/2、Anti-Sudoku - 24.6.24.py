Anti-Sudoku
"""
题目链接:
  https://codeforces.com/contest/1335/problem/D
思路：1300
	读入的是字符串，坑死
	只需要找到每个字符并且替换就好
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    for i in range(9):
        print(input().replace("1","9"))

