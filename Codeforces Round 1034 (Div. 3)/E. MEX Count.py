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

t = int(input())

def solve():
    n = int(input())
    a_lst = list(map(int, input().split()))
    a_lst.sort()
    
    cnt = Counter(a_lst)
    
    for m in range(1, n + 1):
        if m not in cnt:
            print(m)
            continue
    
    m0 = 0
    while cnt[m0] > 0:
        m0 += 1
    
    diff = [0] * (n + 2)
    for i in range(n + 1):
        if i <= m0:
            l = cnt[i]
            r = n - i
            if r < l:
                continue
            diff[l] += 1
            if r + 1 <= n:
                diff[r + 1] -= 1
    
    res = [0] * (n + 2)
    for i in range(1, n + 2):
        res[i] = res[i - 1] + diff[i - 1]
    
    return res[1:]

ans = []
for _ in range(t):
    ans.append(solve())

# print('-' * 50)
for a in ans:
    print(*a)