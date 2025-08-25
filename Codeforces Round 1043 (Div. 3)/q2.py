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
    res = set()
    
    temp = 10
    while temp <= n:
        d = 1 + temp
        if d > n:
            break
        if n % d == 0:
            x = n // d
            res.add(x)
        nxt = temp * 10
        temp = nxt
    
    if not res:
        return [0]
    else:
        return [len(res)] + sorted(res)

ans = []
for _ in range(t):
    ans.append(solve())

for i in ans:
    if i[0] == 0:
        print(0)
    else:
        print(i[0])
        print(*i[1:])