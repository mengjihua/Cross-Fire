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
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b

n = int(input())
g = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

fas = [-1] * (n + 1)
def dfs(u, fa):
    fas[u] = fa
    for v in g[u]:
        if v != fa:
            dfs(v, u)
dfs(n, -1)

ans = 0
for fa in range(1, n + 1):
    stack = [fa]
    vis = [False] * (n + 1)
    sub_tree = []
    
    while stack:
        u = stack.pop()
        sub_tree.append(u)
        for v in g[u]:
            if not vis[v] and v != fas[u]:
                vis[v] = True
                stack.append(v)
    
    sub_tree.sort()
    for i in range(1, len(sub_tree) + 1):
        if sub_tree[i - 1] == i:
            ans += 1
print(ans)