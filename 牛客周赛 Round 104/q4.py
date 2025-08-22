from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b

# TODO: 优化
n, m = map(int, input().split())
g = []
pos = defaultdict(list)
for i in range(n):
    lst = list(map(int, input().split()))
    g.append(lst)

ans = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if g[i - 1][j - 1] == min(i, j):
            ans += 1
        else:
            pos[g[i - 1][j - 1]].append((i, j))

extra = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if g[i - 1][j - 1] == min(i, j):
            continue
        else:
            temp = min(i, j)
            if extra == 2 or temp not in pos:
                continue
            for x, y in pos[temp]:
                add = 1
                if g[x - 1][y - 1] == min(x, y):
                    add -= 1
                if g[i - 1][j - 1] == _min(x, y):
                    add += 1
                extra = _max(extra, add)
print(ans + extra)