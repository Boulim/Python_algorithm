Knapsack
"""
题目链接:https://codeforces.com/problemset/problem/1446/A
思路：（1300）
找数组保存值和下标，按照值进行从大到小排序，尽量快点找到满足解。循环遍历排序后的值，
如果和之前的加和小于m，就加和，并记录下标。
遍历完成后，如果数组和小于m // 2，就返回 -1。满足题意的情况下，ans数组长度就是m，ans里每个值就是操作的下标。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [[a[i],i + 1] for i in range(n)]
    a.sort(key = lambda p:p[0],reverse = True)
    s = 0
    ans = []
    for i in range(n):
        if s + a[i][0] <= m:
            s += a[i][0]
            ans.append(a[i][1])
    if s < (m + 1) // 2:
        print('-1')
    else:
        print(len(ans))
        print(*ans)

