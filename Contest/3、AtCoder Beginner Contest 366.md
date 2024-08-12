# [AtCoder Beginner Contest 366](https://atcoder.jp/contests/abc366)
- 每道题目的链接在文末

- Date：2024.00.11

- 赛后模拟没有排名
  
       
---
> [A、Election 2](https://atcoder.jp/contests/abc366/tasks/abc366_a)

**思路:** 如果有一方的票数已经超过半数， 那么结局就已经确定了。   

`Python代码：`
```Python []
n, a, b = map(int, input().split())
print("Yes" if max(a,b) * 2 > n else "No")
```
<br></br>

> [B、Vertical Writing](https://atcoder.jp/contests/abc366/tasks/abc366_b)

**思路:** 找出字符串长度的最大值， 之后从前往后遍历， 比较相邻字符串的长度，如果前一个比后一个长， 那就在后一个加上相对长度的 '*' 。

从后到前遍历， 分别打印每一列。 只有当列数在这个字符串长度内，才会打印这个字符。

每一列输出， 字符以 '' 结尾。 列输出完， 用`print()`换行。

`Python代码：`
```Python []
n = int(input())
a = []
m = 0
for i in range(n):
    a.append(list(input()))
    m = max(m,len(a[i]))

for i in range(1, n):
    pre = len(a[i - 1])
    cur = len(a[i])
    for _ in range(max(pre - cur, 0)):
        a[i].append('*')
for i in range(m):
    for j in range(n - 1, -1, -1):
        if len(a[j]) > i:
            print(a[j][i], end = '')
    print()
```
<br></br>

> [C、Balls and Bag Query](https://atcoder.jp/contests/abc366/tasks/abc366_c)

**思路:** 用 python 的 `Counter` 来记录每个数出现的次数。

新加入元素时， 直接让其数量加 1 就好， 删除元素也不用从 Counter 中删去。 

用一个变量 `ans` 来记录 Counter 中的元素个数， 每次询问只需要打印变量即可

`Python代码：`
```Python []
from collections import Counter
c = Counter()
ans = 0
for _ in range(int(input())):
    s = input().split()

    if s[0] == '1':
        c[s[1]] += 1
        if c[s[1]] == 1:
            ans += 1
    elif s[0] == '2':
        if c[s[1]] == 1:
            ans -= 1
        c[s[1]] -=1
    elif s[0] == '3':
        print(ans)
```
<br></br>

>  [D、Cuboid Sum Query](https://atcoder.jp/contests/abc366/tasks/abc366_d)

**思路:** 三维前缀和，需要从 3 个坐标轴的方向依次求和。

再从三个坐标轴的方向依次取三维的体积和

`Python代码：`
```Python []
n = int(input())
a = [[list(map(int,input().split())) for _ in range(n)] for _ in range(n)]

pref = [[[0 for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]


for i in range(n):
    for j in range(n):
        for k in range(n):
            pref[i+1][j+1][k+1] = pref[i+1][j+1][k] + pref[i+1][j][k+1] + pref[i][j+1][k+1] - pref[i+1][j][k] - pref[i][j+1][k] - pref[i][j][k+1] + pref[i][j][k] + a[i][j][k]

for _ in range(int(input())):
    x1,x2,y1,y2,z1,z2 = map(int,input().split())
    print(pref[x2][y2][z2] - pref[x1-1][y2][z2] - pref[x2][y1-1][z2] - pref[x2][y2][z1-1] + pref[x1-1][y1-1][z2] + pref[x1-1][y2][z1-1] + pref[x2][y1-1][z1-1] - pref[x1-1][y1-1][z1-1])
```
<br></br>

>  [E、Manhattan Multifocal Ellipse](https://atcoder.jp/contests/abc366/tasks/abc366_e)

**思路:** 对距离的求值再求和， 可以转化为在数轴上每一点的求和。

将坐标统一平移到大于 0 的区域。 平移距离为 d 最大 + 坐标最大。 平移之后进行排序。

对 x 坐标轴方向和 y 坐标轴方向， 每个坐标分别计算距离值，并存到数组中。

再对 y 进行排序， 找 d - x 的值在 y 中的下标， 答案对符合情况的下标值求和， 也就是对数量求和。
`Python代码：`
```Python []
import sys
input = lambda:sys.stdin.readline().strip()
from bisect import bisect_right
n, d = map(int, input().split())
idx = []
idy = []
M = 10 ** 6
for _ in range(n):
    x, y = map(int, input().split())
    idx.append(x + 2 * M)
    idy.append(y + 2 * M)
idx.sort()
idy.sort()

def find(a):
    ans = [0] * (4 * M + 1)
    ans[0] = sum(a)
    x = 0
    for i in range(1, 4 * M + 1):
        ans[i] = ans[i - 1] + 2 * x - n
        while x < n and a[x] == i:
            x += 1
    return ans

fx = find(idx)
fy = find(idy)
fy.sort()
ans = 0
for i in fx:
    ans += bisect_right(fy, d - i)
print(ans)
```
<br></br>

>  [F、Maximum Composition](https://atcoder.jp/contests/abc366/tasks/abc366_f)

**思路:** 把题目给的式子进行化简， 得到一个关于下标的不等式。

按照不等式的大小对下标进行排序， 得出优先级。

再对优先级利用动态规划求出最大值。 因为直接按照优先级的前 k 个不一定是最优解。

`Python代码：`
```Python []
import sys
input = lambda:sys.stdin.readline().strip()

A = []
B = []
n, k = map(int, input().split())
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

s = sorted(range(n), key = lambda i: (A[i] - 1) / B[i])

ans = [0] * (k + 1)
ans[0] = 1

for i in s:
    for j in range(k, 0, -1):
        ans[j] = max(ans[j], A[i] * ans[j - 1] + B[i])
print(ans[k])
```
<br></br>

>  [G、XOR Neighbors](https://atcoder.jp/contests/abc366/tasks/abc366_g)

**思路:** 高斯消元

消元之后不知道干嘛了

`Python代码：`
```Python []
None
```
<br></br>
## 题目

| 题号 | 题目 | 链接 |
|-|-|-|
| A | Election 2 | [A、Election 2](https://atcoder.jp/contests/abc366/tasks/abc366_a) |
| B | Vertical Writing | [B、Vertical Writing](https://atcoder.jp/contests/abc366/tasks/abc366_b) |
| C | Balls and Bag Query | [C、Balls and Bag Query](https://atcoder.jp/contests/abc366/tasks/abc366_c) |
| D | Cuboid Sum Query | [D、Cuboid Sum Query](https://atcoder.jp/contests/abc366/tasks/abc366_d) |
| E | Manhattan Multifocal Ellipse | [E、Manhattan Multifocal Ellipse](https://atcoder.jp/contests/abc366/tasks/abc366_e) |
| F | Maximum Composition | [F、Maximum Composition](https://atcoder.jp/contests/abc366/tasks/abc366_f) |
| G | XOR Neighbors | [G、XOR Neighbors](https://atcoder.jp/contests/abc366/tasks/abc366_g) |
