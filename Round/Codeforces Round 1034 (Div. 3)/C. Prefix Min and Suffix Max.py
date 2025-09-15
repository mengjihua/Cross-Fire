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
        
    pre_min = [0] * n
    suf_max = [0] * n
        
    pre_min[0] = a_lst[0]
    for i in range(1, n):
        pre_min[i] = min(pre_min[i - 1], a_lst[i])
        
    suf_max[n-1] = a_lst[n-1]
    for i in range(n - 2, -1, -1):
        suf_max[i] = max(suf_max[i + 1], a_lst[i])
        
    res = []
    for i in range(n):
        if a_lst[i] == pre_min[i] or a_lst[i] == suf_max[i]:
            res.append('1')
        else:
            res.append('0')
        
    print(''.join(res))