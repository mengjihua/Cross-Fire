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

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(len(a)):
    suba = []
    for j in range(i, len(a)):
        suba.append(a[j])
        suba.sort()
        for k in range(1, len(suba) + 1):
            if suba[k - 1] == k:
                ans += 1
print(ans)