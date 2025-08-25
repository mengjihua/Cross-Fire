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
from random import getrandbits
setrecursionlimit(5 * 10 ** 4 + 1)
input = lambda: stdin.readline().rstrip()
RD = getrandbits(31)
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b

t = int(input())

def get_score(num):
    num_score = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1]
    res = 0
    while num > 0:
        digit = num % 10
        res += num_score[digit]
        num //= 10
    return res


temp = [4, 8, 48, 88, 488, 888]

def solve():
    n, sm = map(int, input().split())
    idx = bisect_left(temp, sm // n)
    
    ans = []
    mx = 0
    def dfs(i, score, remain, path):
        nonlocal mx, ans
        if i == n:
            if mx < score:
                mx = score
                ans = path
            return
        for num in temp[idx - 1:idx + 2]:
            if num > remain:
                continue
            dfs(i + 1, score + get_score(num), remain - num, path + [num])

    dfs(0, 0, sm, [])
    return ans

ans = []
for _ in range(t):
    ans.append(solve())
for i in ans:
    if not i:
        print(-1)
    else:
        print(*i)