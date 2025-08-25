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

t = int(input())

def find(L, R, d):
    l = L % 10
    diff = (d - l) % 10
    r = L + diff
    return r if r <= R else -1

def solve():
    n, L1, R1, L2, R2 = map(int, input().split())
    a = list(map(int, input().split()))
    
    for i in range(n - 4):
        temp = a[i] * a[i + 1] % 10
        if temp != a[i + 2]:
            return "-1 -1"
    
    ans = []
    if n == 3:
        for a1 in range(10):
            for a2 in range(10):
                a3 = (a1 * a2) % 10
                if a3 != a[0]:
                    continue
                
                ans1 = find(L1, R1, a1)
                if ans1 == -1: continue
                ans2 = find(L2, R2, a2)
                if ans2 == -1: continue

                if not ans or [ans1, ans2] < ans:
                    ans = [ans1, ans2]
    else:
        for a1 in range(10):
            for a2 in range(10):
                a3 = (a1 * a2) % 10
                
                if a3 != a[0] or (a2 * a3) % 10 != a[1]:
                    continue

                ans1 = find(L1, R1, a1)
                if ans1 == -1: continue
                ans2 = find(L2, R2, a2)
                if ans2 == -1: continue

                if not ans or [ans1, ans2] < ans:
                    ans = [ans1, ans2]

    return f'{ans[0]} {ans[1]}' if ans else '-1 -1'


ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')