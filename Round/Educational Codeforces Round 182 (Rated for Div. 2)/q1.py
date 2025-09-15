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
    a = list(map(int, input().split()))
    
    pre = [0] * (n + 1)
    for i in range(1, n + 1):
        pre[i] = pre[i - 1] + a[i - 1]
    
    for l in range(1, n - 1):
        for r in range(l + 1, n):
            s1 = pre[l] % 3
            s2 = (pre[r] - pre[l]) % 3
            s3 = (pre[n] - pre[r]) % 3
            
            if s1 == s2 == s3:
                return f"{l} {r}"
            if s1 != s2 and s2 != s3 and s1 != s3:
                return f"{l} {r}"
    return "0 0"

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')