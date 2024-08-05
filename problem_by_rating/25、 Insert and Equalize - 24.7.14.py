Insert and Equalize
"""
题目链接:
https://codeforces.com/contest/1902/problem/C
思路：（1300）
每次减去的数，是最大数与当前数的最大公约数，需要找到共同的最大公因数，就是x
再考虑添加an+1，如果比max大，则答案要+数组长度这么大的值，考虑从最大值开始减去x，如果当前数存在，再减去一个x，直到减去k个x后，当前数不存在。就把max-kx当作an+1插入，再统计和，即最大值减去当前值，除以公因数x，作为答案。
"""
Python代码:
#x是最大公约数
#再看an+1怎么选，最大值减去x
#如果是减去，计算结果+1，遍历数组长度，减去的最大长度为数组长度+1
import sys
input = lambda:sys.stdin.readline().strip()
from math import gcd
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if n == 1:
        print('1')
        continue
    ma = max(a)
    s = set(a)
    a = [ma - x for x in a]
    g = 0
    for i in range(1,n):
        g = gcd(g,a[i] - a[i - 1])
    x = ma - g    
    while x in s:
        x -= g
    a.append(ma - x)
    print(sum(x // g for x in a))

