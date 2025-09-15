from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 5 + 1)

t = int(input())

def solve():
    n, k = map(int, input().split())
    
    lst = []
    for _ in range(n):
        l, r, real = map(int, input().split())
        lst.append((l, r, real))
    lst.sort()
    
    # max_coins = k
    # visited = set([k])
    # q = deque([k])
    # visited = set()

    # while q:
    #     coins = q.popleft()
    #     for l, r, real in lst:
    #         if l <= coins <= r and real not in visited:
    #             visited.add(real)
    #             q.append(real)
    #             if real > max_coins:
    #                 max_coins = real
    
    heap = []
    max_coins = k

    i = 0
    while True:
        changed = False 
        while i < n and lst[i][0] <= max_coins:
            l, r, real = lst[i]
            if l <= max_coins <= r and real > max_coins:
                heappush(heap, -real)
            i += 1

        if heap:
            real = -heappop(heap)
            max_coins = max(max_coins, real)
            changed = True

        if not changed:
            break
        
    return max_coins

ans = []
for _ in range(t):
    ans.append(solve())

for i in ans:
    print(i)