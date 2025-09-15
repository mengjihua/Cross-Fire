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
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b

t = int(input())

def solve():
    n = int(input())
    res = []
    for i in range(1, n + 1):
        if i % 2 == 1:
            res.append(-1)
        else:
            res.append(2 if i == n else 3)
    return ' '.join(map(str, res))

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')