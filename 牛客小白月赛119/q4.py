from typing import List
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10 ** 5 + 1)


def solve():
    n = int(input())
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    
    sekai = []
    for i in range(1, n + 1):
        if len(g[i]) == 1:
            sekai.append(i)
    
    dis = [-1] * (n + 1)
    q = deque()
    for i in sekai:
        dis[i] = 0
        q.append(i)
    
    while q:
        u = q.popleft()
        for v in g[u]:
            if dis[v] == -1:
                dis[v] = dis[u] + 1
                q.append(v)
    
    max_len = -1
    for i in range(1, n + 1):
        if dis[i] != 0 and dis[i] > max_len:
            max_len = dis[i]
            
    res = []
    for i in range(1, n + 1):
        if dis[i] == max_len:
            res.append(i)
    return sorted(res)

ans = []
t = int(input())
for _ in range(t):
    ans.append(solve())

for i in ans:
    print(len(i))
    print(*i)