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
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)


t = int(input())

def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    
    adj = [0] * n
    for i in range(1, n):
        if a[i] == a[i - 1]:
            adj[i] = 1
    
    prefix_adj = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_adj[i] = prefix_adj[i - 1] + adj[i - 1]
    
    pre0 = [0] * (n + 1)
    pre1 = [0] * (n + 1)
    for i in range(1, n + 1):
        pre0[i] = pre0[i - 1] + (1 if a[i - 1] == 0 else 0)
        pre1[i] = pre1[i - 1] + (1 if a[i - 1] == 1 else 0)
    
    res = []
    for _ in range(q):
        l, r = map(int, input().split())
        cnt0 = pre0[r] - pre0[l - 1]
        cnt1 = pre1[r] - pre1[l - 1]
        
        if cnt0 % 3 != 0 or cnt1 % 3 != 0:
            res.append("-1")
        else:
            sm = cnt0 + cnt1
            base = sm // 3
            if prefix_adj[r] - prefix_adj[l] == 0:
                base += 1
            res.append(str(base))
    return res

ans = []
for _ in range(t):
    ans.append(solve())
for res in ans:
    print(*res, sep='\n')