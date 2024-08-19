 No to Palindromes!
"""
题目链接：https://codeforces.com/contest/464/problem/A

思路：检查相邻的两个或者间隔一个的两个是否有相同的。遍历从最后一个开始

将字符转化为数字进行处理，处理结束再转化为字符。

由于数据范围小，直接暴力即可

"""
# python代码：
# 不包含相邻的两个，或者相隔的三个
import sys
input = lambda:sys.stdin.readline().strip()

n, p = map(int, input().split())
s = [ord(c) - ord('a') for c in input()]

for i in range(n - 1, -1, -1):
    for c in range(s[i] + 1, p):
        for j in range(1, 3):
            if i - j >= 0 and s[i - j] == c:
                break
        else:
            s[i] = c
            for idx in range(i + 1, n):
                for c in range(p):
                    for j in range(1, 3):
                        if idx - j >= 0 and s[idx - j] == c:
                            break
                    else:
                        s[idx] = c
                        break
            print(''.join(chr(x + ord('a')) for x in s))
            exit()
else:
    print('NO')
