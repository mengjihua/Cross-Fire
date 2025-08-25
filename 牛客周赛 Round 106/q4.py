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


def var(x):
    res = {}
    cur = x
    for steps in range(11):
        if cur not in res:
            res[cur] = steps
        cur = cur ^ (cur // 2)
    return res

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    num_var_k = []
    for x in a:
        num_var_k.append(var(x))
    
    ans = inf
    
    def dfs(i, current, cnt):
        nonlocal ans
        if i == n:
            if current == current[::-1]:
                ans = _min(ans, cnt)
            return
        
        for val, k_cnt in num_var_k[i].items():
            current.append(val)
            dfs(i + 1, current, cnt + k_cnt)
            current.pop()
    
    dfs(0, [], 0)
    
    return ans if ans != inf else -1

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')