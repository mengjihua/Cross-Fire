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

MOD = 998244353

t = int(input())

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    op = []
    for i in range(n):
        op.append([(a[i], b[i]), (b[i], a[i])])
    
    remain = swap = 1
    for i in range(1, n):
        nxt_remain = nxt_swap = 0
        a0, b0 = op[i - 1][0]
        a1, b1 = op[i - 1][1]
        nxt_a0, nxt_b0 = op[i][0]
        nxt_a1, nxt_b1 = op[i][1]
        
        if a0 <= nxt_a0 and b0 <= nxt_b0:
            nxt_remain = remain
        if a1 <= nxt_a0 and b1 <= nxt_b0:
            nxt_remain += swap
            
        if a0 <= nxt_a1 and b0 <= nxt_b1:
            nxt_swap = remain
        if a1 <= nxt_a1 and b1 <= nxt_b1:
            nxt_swap += swap

        remain, swap = nxt_remain % MOD, nxt_swap % MOD
    
    return (remain + swap) % MOD
    

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')