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

n, k = map(int, input().split())

# TODO: 特解: n - k == 1
if n < k or n - k == 1:
    print(-1)
else:
    lst = []
    for i in range(1, k + 1):
        lst.append(i)
    if n != k:
        lst.extend([n] + [i for i in range(k + 1, n)])
    print(*lst)