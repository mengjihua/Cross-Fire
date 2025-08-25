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
    
    cur = n
    if int(str(cur)[::-1]) == cur:
        return cur, 0
    
    for step in range(1, k + 1):
        rev = int(str(cur)[::-1])
        cur = cur + rev
        if int(str(cur)[::-1]) == cur:
            return f'{cur} {step}'

    return f'{cur} {-1}'


ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')