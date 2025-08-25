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
    
    a_to_bi = [0] * 31
    for i in range(n):
        for j in range(31):
            a_to_bi[j] += (a_lst[i] >> j) & 1
    # print(a_to_bi[:5])
    
    ans = 0
    for a in a_lst:
        temp = 0
        for j in range(31):
            if (a >> j) & 1:
                temp += (n - a_to_bi[j]) * (1 << j)
            else:
                temp += a_to_bi[j] * (1 << j)
        ans = max(ans, temp)
    print(ans)