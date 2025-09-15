from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
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
    p = list(map(int, input().split()))

    zero_pos = [i for i, x in enumerate(p) if x == 0]
    exist = [False] * (n + 1)
    for x in p:
        if x > 0:
            exist[x] = True
    missing = [x for x in range(1, n + 1) if not exist[x]]
    
    if len(zero_pos) == 1 and len(missing) == 1 and missing[0] == zero_pos[0] + 1:
        p[zero_pos[0]] = missing[0]
    
    pos = [i for i in range(n) if p[i] != i + 1]
    
    return pos[-1] - pos[0] + 1 if pos else 0

ans = []
for _ in range(t):
    ans.append(solve())

print('\n'.join(map(str, ans)))