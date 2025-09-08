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
    n = int(input())
    b = list(map(int, input().split()))
    
    if sum(set(b)) > n:
        return -1
    
    g = defaultdict(list)
    for i, k in enumerate(b):
        g[k].append(i)
    
    valid = True
    for k in range(1, n + 1):
        if len(g[k]) % k != 0:
            valid = False
            break
            
    if not valid:
        return -1
    
    ans = [0] * n
    nxt = 1
    for k, lst in g.items():
        if not lst:
            continue
        m = len(lst) // k
        for i in range(m):
            start = i * k
            for j in range(k):
                pos = lst[start + j]
                ans[pos] = nxt
            nxt += 1
    return ' '.join(map(str, ans))


ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')