Di-visible Confusion
"""
题目链接:https://codeforces.com/problemset/problem/1603/A
思路：（1300）
查阅每个ai是不是能被（2, i+ 1）整除。对于每个 i 来说，从 2到 𝑖+1之间至少有一个整数，
使得 𝑎𝑖 不能被该整数整除。如果对于某个整数 𝑖 来说，它不被满足，那么就肯定没有解。否则，解总是存在的。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _  in range(int(input())):
    n = int(input())
    a = [0] + list(map(int,input().split()))
    for i in range(1, n + 1):
        for j in range(i + 1, 1, -1):
            if a[i] % j:
                break
        else:
            print("NO") 
            break          
    else:
        print("YES")

