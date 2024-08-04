Sofia and the Lost Operations
"""
题目链接:
https://codeforces.com/contest/1980/problem/C
思路：（1300）
找出值不同的，组成数组diff。在变化数组中看是否所有的不同diff都在变化的数组d中，
并且最后一个变化是否在答案b中，在就可以最后收尾。都满足返回yes，否则返回no
另外也可以用3.10的counter进行比较返回。
"""
Python代码1:
import sys
input = lambda:sys.stdin.readline().strip()
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    m = int(input())
    d = list(map(int,input().split()))
    diff = [y for x,y in zip(a,b) if x != y]
    i,j = 0,0
    c = d[-1]
    d.sort()
    diff.sort()
    while i < len(diff) and j < m:
        if diff[i] == d[j]:
            i += 1
        j += 1
    #如果所有不同的值，都在变化数组d里。并且变化数组的最后一个，在结果b数组中，就可以收尾了。
    if i == len(diff) and c in b: 
        print("YES")
    else:
        print("NO")

Python代码2:
import sys
input = lambda:sys.stdin.readline().strip()
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a_arr = input().split()
    b_arr = input().split() 
    input()
    d_arr = input().split()
    diff = [y for x,y in zip(a_arr,b_arr) if x!=y]
    if Counter(diff) <= Counter(d_arr) and d_arr[-1] in b_arr:
        print("YES")
    else:
        print("NO")



