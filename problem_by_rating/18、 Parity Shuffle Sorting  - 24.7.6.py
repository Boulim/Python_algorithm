 Parity Shuffle Sorting
"""
题目链接:
https://codeforces.com/problemset/problem/1733/C
思路：（1300）
奇数换右，偶数换左。能不能通过第一个数，把所有数变完。把数列只换成第一个数
	第一个是偶数，找奇数全换了，剩下全偶数，找最后一个全换
	第一个是奇数，找偶数全换了，剩下全奇数，找最后一个换完。
所以只需要关注第一个数和最后一个数就可以。
把这俩数换成同一个数。找剩余的数，和这个数加为奇数，找第一个数换，为偶数，找最后一个数换。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(n - 1)
    if n > 1:
        x = a[0] if (a[0] + a[n - 1])% 2 else a[n - 1]
        print(1,n)
    for t in range(1, n - 1):
        if (a[t] + x) % 2 == 1:
            print(1, t + 1)
        else:
            print(t + 1,n)
"""
尝试下只找第一个数行不行。其实可以假装替换。
如果0和n-1位加为偶数，把左边的换了，其实这俩都是奇数，不影响和中间数相加的奇偶性，可以用a[0]代替a[n - 1]。
如果加为奇数，把右边的值换为a[0]。
综上所述，代码可以改为：
"""
Python代码2:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(n - 1)
    if n > 1:
        print(1,n)
    for t in range(1, n - 1):
        if (a[0] + a[t]) % 2:
            print(1, t + 1)
        else:
            print(t + 1,n)


