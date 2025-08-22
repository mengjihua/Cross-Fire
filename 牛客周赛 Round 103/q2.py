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
def input(): return stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b


t = int(input())


def solve():
    n = int(input())
    lst = list(map(int, input().split()))

    last, lidx = -inf, -1
    for i in lst:
        if i >= last:
            last = i
            lidx += 1
        else:
            break

    if lidx == n - 1:
        return 'YES'
    else:
        judge = True
        last = -inf
        for i in range(lidx + 1, n):
            if lst[i] < last:
                judge = False
                break
            last = lst[i]
        if judge and lst[-1] <= lst[0]:
            return 'YES'
        else:
            return 'NO'


ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')
