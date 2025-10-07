from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

t = int(input())

def solve():
    a, b, k = map(int, sys.stdin.readline().split())
    g = gcd(a, b)
    dx, dy = a // g, b // g
    if dx <= k and dy <= k:
        return 1
    return 2

ans = []
for _ in range(t):
    ans.append(solve())

for i in ans:
    print(i)