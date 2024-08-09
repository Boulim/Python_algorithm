# [Codeforces Round 964 (Div. 4)](https://codeforces.com/contest/1999)
- 每道题目的链接在文末

- Date：2024.08.09

- 赛后模拟没有排名
  
       
---
> [A、 A+B Again?](https://codeforces.com/contest/1999/problem/A)

**思路:** 分别取出`个位`和`十位`的数字

输出二者相加的和

`Python代码：`
```Python []
for _ in range(int(input())):
    n = int(input())
    print(n % 10 + n // 10)
```
<br></br>
> [B、Card Game](https://codeforces.com/contest/1999/problem/B)

**思路:** 共 4 场比赛，每场比赛有两个结果。依次枚举。

suneet 获胜的情况分为： 赢一局，平一局，或者全赢。   

`Python代码：`
```Python []
for _ in range(int(input())):
    a1, a2, b1, b2 = map(int, input().split())
    ans = 0
    if a1 >= b1 and a2 >= b2 and not (a1 == b1 and a2 == b2):
        ans += 2
    if a2 >= b1 and a1 >= b2 and not (a2 == b1 and a1 == b2):
        ans += 2
    print(ans)
```
<br></br>

> [C、Showering](https://codeforces.com/contest/1999/problem/C)

**思路:** 分别判断每个区间的开始和结束的间隔，是否 `>=s`。

再判断第一段的开始和总开始时间，最后一段的结束和总结束时间的时间间隔是否 `>=s`。

如果存在满足条件的情况，打印`YES`, 否则打印 `NO` 。

`Python代码：`
```Python []
import sys
input = lambda:sys.stdin.readline().strip()

for _ in range(int(input())):
    n, s, m = map(int, input().split())
    pre = 0
    flag = 0
    for _ in range(n):
        l, r = map(int, input().split())
        if l - pre >= s:
            flag = 1
        pre = r
    if flag or m - pre >= s:
        print("YES")
    else:
        print("NO")
```
<br></br>

>  [D、Slavic's Exam](https://codeforces.com/contest/1999/problem/D)

**思路:** 看 `s` 中是否包含 `t` 的每一个字符就好。

判断 `t` 的每个字符是否存在 `s`中。

如果是 `?` 并且 `t`还没判断完， 在答案中加入 `t` 的字符。 如果判断完了， 答案加入 `a` 。

最后看`t`是否被遍历完，选择打印 `YES` 或者 `NO`.

**注意:**因为 python 的 string 不可以更改，而新建字符串的代价为字符串长度。

这里用数组存字符，在输出时用`''.join()` 函数打印字符串。

不在读入加，是因为读入的时候，也是新建立一个数组。

`Python代码：`
```Python []
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    s = input()
    t = input()
    n, m = len(s), len(t)
    j = 0
    q = []
    for i in range(n):
        if j < m:
            if s[i] == t[j] or s[i] == '?':
                q.append(t[j])
                j += 1
            else:
                q.append(s[i])
        else:
            if s[i] != '?':
                q.append(s[i])
            else:
                q.append('a')
    if j >= m:
        print("YES")
        print(''.join(q))
    else:
        print("NO")
```
<br></br>


>   [E、Triple Operations](https://codeforces.com/contest/1999/problem/E)

**思路:** 处理过程为先处理第一个，让其变成0， 再遍历处理。

在处理第一个时，直接除以 3 ， 让操作数量 +2， 接着处理其他操作时， +1 就好。但是这样会超时。

将数组按照 `3 的幂` 划分成段， 每一段的数字操作次数都是一样的，这样就可以直接处理一堆数。

通过第一个数确定起始的 `3 的幂次` 和 ` 操作次数` , 再比较 r 和 3 的幂 大小关系，来确定处理的范围。

每次处理，让答案加上`长度 * 操作次数` ，最后一段单独处理， 输出答案

`Python代码：`
```Python []
import sys
input = lambda:sys.stdin.readline().strip()

for _ in range(int(input())):
    l, r = map(int, input().split())
    t = l
    base = 1 # 3 的幂次
    cnt = 0 #处理次数
    sum = 0 #次数总和
    while t:
        t //= 3
        sum += 2
        cnt += 1
        base *= 3
    while r >= base:
        sum += (base - 1 - l) * cnt
        l = base - 1
        base *= 3
        cnt += 1
    sum += (r - l) * cnt
    print(sum)
```
<br></br>

>   [F、Expected Median](https://codeforces.com/contest/1999/problem/F)

**思路:** 预先处理组合数，减少复杂度

组合数学，中位数实际上是比较的 0 和 1 谁的个数多。于是可以统计 1 的个数。

从 k 个中，只要选 `> k // 2` 个 1， 那么答案就可以 + 1.

于是可以用组合数直接求出答案。

`Python代码：`
```Python []
mod = 10 **9 + 7
f = [1]
for j in range(1,200001):
    f.append((f[-1] * j) % mod)
def c(n,k):
    return (f[n] * pow(f[k] * f[n-k], -1, mod)) % mod
    #三个参数：底数、指数和可选的模数。
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    c1 = a.count(1)
    c0 = n - c1
    cnt = 0
    for j in range(k // 2 + 1, min(c1, k) + 1):
        if k - j <= n - c1: # 应选 0 的个数 <= 0 的总个数
            cnt += c(c1 , j) * c(c0, k - j)
        cnt %= mod
    print(cnt % mod)
```
<br></br>

>   [G1、 Ruler (easy version)](https://codeforces.com/contest/1999/problem/G1)

**思路:** 板正的二分题。

每次都选取 1 和 中位数 mid 进行测试。 

如果答案正确，让 l = mid + 1， 答案错误， 让 r = mid 。 

直到找到最小的错误的数， 输出 r 。

**注意:** 交互式的题不能快读，快读会出错。

`Python代码：`
```Python []
import sys

for _ in range(int(input())):
    l = 2
    r = 999
    while l < r:
        mid = (l + r) // 2
        print('?', mid, 1)
        x = int(input())
        if x == mid:
            l = mid + 1
        else:
            r = mid
    print('!', r)
```
<br></br>

>   [G2、Ruler (hard version)](https://codeforces.com/contest/1999/problem/G2)

**思路:** 三分题。

思路和过程同上题， 直接上代码。

`Python代码：`
```Python []
for _ in range(int(input())):
    l, r = 2, 999
    while l < r:
        a = l + (r - l) // 3
        b = l + (r - l) // 3 * 2
        print('?', a, b, flush = True)
        p = int(input())
        if p == (a + 1) * (b + 1): # 两个数都错了
            r = a
        elif p == a * b: # 两个数都对了
            l = b + 1
        else: # 错一个
            l = a + 1
            r = b
  print('!', l, flush = True)
```
<br></br>
## 题目

| 题号 | 问题 | 链接 |
| -------- | -------- | -------- |
| A | A+B Again? | [A、 A+B Again?](https://codeforces.com/contest/1999/problem/A) |
| B | Card Game | [B、Card Game](https://codeforces.com/contest/1999/problem/B) |
| C | Showering | [C、Showering](https://codeforces.com/contest/1999/problem/C) |
| D | Slavic's Exam | [D、Slavic's Exam](https://codeforces.com/contest/1999/problem/D) |
| E | Triple Operations | [E、Triple Operations](https://codeforces.com/contest/1999/problem/E) |
| F | Expected Median | [F、Expected Median](https://codeforces.com/contest/1999/problem/F) |
| G1 |Ruler (easy version) | [G1、 Ruler (easy version)](https://codeforces.com/contest/1999/problem/G1) |
| G2 |Ruler (hard version) | [G2、Ruler (hard version)](https://codeforces.com/contest/1999/problem/G2) |
