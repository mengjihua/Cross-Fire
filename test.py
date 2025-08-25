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
for _ in range(t):
    n = int(input())
    a_lst = list(map(int, input().split()))
        
    cnt = [0] * (n + 2)
    for num in a_lst:
        cnt[num] += 1
        
    m = 0
    while cnt[m] > 0:
        m += 1
         
    max_possible_k = n
    diff = [0] * (n + 2)
        
    for x in range(0, n + 1):
        if x < m:
            min_k = cnt[x]
            max_k = n - x
            if min_k > max_k:
                continue
            diff[min_k] += 1
            if max_k + 1 <= n:
                diff[max_k + 1] -= 1
        else:
            max_k = n - x
            if max_k < 0:
                continue
            diff[0] += 1
            if max_k + 1 <= n:
                diff[max_k + 1] -= 1
        
    ans = [0] * (n + 1)
    current = 0
    for k in range(0, n + 1):
        current += diff[k]
        ans[k] = current
        
    print(' '.join(map(str, ans)))