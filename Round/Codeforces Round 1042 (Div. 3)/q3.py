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

# def solve():
#     n, k = map(int, input().split())
#     s = list(map(int, input().split()))
#     t = list(map(int, input().split()))
    
#     map_k = defaultdict(int)
#     for i in range(n):
#         si, ti = s[i] % k, t[i] % k
#         map_k[_min(si, k - si) ^ RD] += 1
#         map_k[_min(ti, k - ti) ^ RD] -= 1
    
#     for i in map_k.keys():
#         if map_k[i] != 0:
#             return 'NO'
#     return 'YES'

# ans = []
# for _ in range(t):
#     ans.append(solve())
    
# print(*ans, sep='\n')


# TODO: 第二种解法, 防止哈希碰撞
for _ in range(t):
    n, k = map(int, input().split())
    
    def get():
        a = list(map(int, input().split()))
        return sorted(_min(x % k, k - x % k) for x in a)
    
    s_sorted = get()
    t_sorted = get()
    
    print("YES" if s_sorted == t_sorted else "NO")