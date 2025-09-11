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

def solve():
    n, k = map(int, input().split())
    w_t = []
    for _ in range(n):
        w, t = map(int, input().split())
        w_t.append(t - w)
    w_t.sort()
    
    cur = max_t = -inf
    for diff in w_t:
        if diff <= cur:
            t = cur
            cur += 1
        else:
            t = diff
            cur = diff + 1
        max_t = _max(max_t, t)
    return max_t + k

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')