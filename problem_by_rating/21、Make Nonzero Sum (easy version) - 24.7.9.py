Make Nonzero Sum (easy version)
"""
题目链接：https://codeforces.com/problemset/problem/1753/A1
21、 Problem - 1753A1 - Codeforces
思路：（1300）
只有元素1和-1，如果数组长度是奇数，则不能凑出来0，返回-1
数组长度为偶数时，按照长度为2进行划分，如果长度为2的两个元素相同，就放到一起，子和为0，划分段数+ 1；
如果两者不同，就放到两个段里，这时两段相加为0，段数+ 2
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2:
        print('-1')
        continue
    ans = []
    for i in range(0,n,2):
        if a[i] == a[i + 1]:
            ans.append([i + 1, i + 2])
        else:
            ans.append([i + 1, i + 1])
            ans.append([i + 2, i + 2])
    print(len(ans))
    for x in ans:
        print(x[0], x[1])


