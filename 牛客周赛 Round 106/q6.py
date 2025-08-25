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
    a = list(map(int, input().split()))
    
    cnt = 0
    # for l in range(n - 2):
    #     for r in range(l + 2, n):
    #         if a[l] == a[r]:
    #             continue
    #         sub_a = a[l:r + 1]
    #         mn = max(sub_a[1:-1])
    #         if sub_a[0] > mn and mn < sub_a[-1]:
    #             cnt += 1
    for l in range(n - 2):
        mx = -inf
        for r in range(l + 2, n):
            if a[l] == a[r]:
                continue
            mx = _max(mx, a[r - 1])
            if a[l] > mx and mx < a[r]:
                cnt += 1

    return cnt

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')