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
setrecursionlimit(5 * 10 ** 4 + 1)
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b

t = int(input())

def solve():
    n = int(input())
    if n == 2:
        input()
        return 0
    if n == 1:
        return 0

    g = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
        
    def bfs(start):
        dis = [-1] * (n + 1)
        q = deque([start])
        dis[start] = 0
        while q:
            u = q.popleft()
            for v in g[u]:
                if dis[v] == -1:
                    dis[v] = dis[u] + 1
                    q.append(v)
        return dis

    dis1 = bfs(1)
    u = 1
    for i in range(1, n + 1):
        if dis1[i] > dis1[u]:
            u = i

    dis2 = bfs(u)
    v = 1
    for i in range(1, n + 1):
        if dis2[i] > dis2[v]:
            v = i
    dm = dis2[v]

    if dm <= 2:
        return 0

    parent = [-1] * (n + 1)
    q = deque([u])
    parent[u] = 0
    while q:
        cur = q.popleft()
        if cur == v:
            break
        for nxt in g[cur]:
            if nxt != parent[cur]:
                parent[nxt] = cur
                q.append(nxt)

    path = []
    cur = v
    while cur:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    deg = [0] * (n + 1)
    for i in range(1, n + 1):
        deg[i] = len(g[i])

    cnt = 0
    for cur in path[1:-1]:
        if deg[cur] > 2:
            cnt += deg[cur] - 2

    return cnt if cnt != 0 else 1

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')