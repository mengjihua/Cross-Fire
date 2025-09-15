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

# https://codeforces.com/problemset/problem/1194/C
q = int(input())

def solve():
    s = input()
    t = input()
    p = input()
    
    if s == t:
        return 'Yes'
    if len(s) + len(p) < len(t):
        return 'No'
    
    # s_cnt = Counter(s)
    # t_cnt = Counter(t)
    p_cnt = Counter(p)

    # if any(s_cnt[c] + p_cnt[c] < t_cnt[c] for c in t_cnt.keys()):
    #     return 'No'
    
    i, j = 0, 0
    while j < len(t):
        if i < len(s) and s[i] == t[j]:
            i, j = i + 1, j + 1
        else:
            if p_cnt[t[j]] == 0:
                return 'No'
            else:
                p_cnt[t[j]] -= 1
                j += 1
            
    return 'Yes' if i == len(s) else 'No'  # a b a 这个样例不判断会出问题

ans = []
for _ in range(q):
    ans.append(solve())
print(*ans, sep='\n')