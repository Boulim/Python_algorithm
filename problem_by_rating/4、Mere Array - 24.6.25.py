Mere Array
"""
题目链接:
https://codeforces.com/problemset/problem/1401/C
思路：（1300）
我们把 a 的最小元素定义为 m 。我们可以发现，不能被 m 整除的元素的位置是不能改变的，因为这些元素没有 m 作为因子。但是我们可以按照下面的方法
重新排列能被 m 整除的元素：
 假设 m = a_x，且有两个元素 a_y , a_z，其中 x ， y， z都不相同。交换（ a_x， a_y ）、交换（ a_y ， a_z ）和交换（ a_z ， a_x）。然后只交换初始状态中的 a_y 和 a_z 。重复此过程。
因此，我们可以按非降序重新排列能被 m 整除的元素。之后，如果整个数组是非递减的，则答案为 YES ，否则为 NO。
时间复杂度 : O(n log n)

这题采用另一个方向，如果某个数不能被m整除，且和原来位置不同，就break打印no。如果都满足，则打印yes
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
from math import gcd
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    c = sorted(a)
    for x,y in zip(a,c):
        if x % c[0] and x !=y:
            print('NO')
            break
    else:
        print('YES')
