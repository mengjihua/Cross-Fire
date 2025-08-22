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
def input(): return stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b


t = int(input())


def solve():
    n, m = map(int, input().split())
    s = list(input())

    t = []
    for _ in range(m):
        t.append(list(input()))

    ans = 0
    for i in range(n):
        cnt = 0
        temp = s[i:]
        for j in range(m):
            tt = t[j]
            p = 0
            while p < len(tt) and p < len(temp):
                if tt[p] == temp[p]:
                    p += 1
                else:
                    break
            cnt += p
        ans = _max(ans, cnt)
    return ans


ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')
