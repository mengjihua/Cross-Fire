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

def solve():
    n, m = map(int, input().split())
    
    g = []
    for _ in range(n):
        g.append(list(input()))
    
    # 0, 0 -> n-1, m-1
    def dijkstra1():
        heap = []
        heappush(heap, (0, 0, 0))
        dis = [[inf] * m for _ in range(n)]
        dis[0][0] = 0
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while heap:
            cost, x, y = heappop(heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and dis[nx][ny] == inf:
                    if cost != 0:
                        n_cost = cost + 1
                    else:
                        n_cost = cost + (g[nx][ny] == '#')
                    dis[nx][ny] = n_cost
                    heappush(heap, (n_cost, nx, ny))
        return dis
    
    
    # n-1, m-1 -> 0, 0
    def dijkstra2():
        heap = []
        heappush(heap, (0, n - 1, m - 1))
        dis = [[inf] * m for _ in range(n)]
        dis[n - 1][m - 1] = 0
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while heap:
            cost, x, y = heappop(heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and dis[nx][ny] == inf:
                    if cost != 0:
                        n_cost = cost + 1
                    else:
                        n_cost = cost + (g[nx][ny] == '#')
                    dis[nx][ny] = n_cost
                    heappush(heap, (n_cost, nx, ny))
        return dis
    
    dis1, dis2 = dijkstra1(), dijkstra2()
    # print(dis1)
    # print(dis2)
    ans = inf
    for i in range(n):
        for j in range(m):
            if g[i][j] == '#':
                ans = _min(ans, dis1[i][j] + dis2[i][j] - 1)
            else:
                ans = _min(ans, dis1[i][j] + dis2[i][j])

    return -1 if ans == inf else ans



ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')