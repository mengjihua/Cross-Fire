from typing import List, Tuple, Dict, Set, Optional
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
    a, b, x, y = map(int, input().split())
    
    if a == b:
        return 0
    
    if a > b:
        if a - b == 1 and a % 2 != 0:
            return y
        else:
            return -1

    # if x <= y:
    #     return (b - a) * x
    # else:
    #     if a % 2 == 0:
    #         return ceil((b - a) / 2) * x + floor((b - a) / 2) * y
    #     else:
    #         return floor((b - a) / 2) * x + ceil((b - a) / 2) * y
    odd_cnt = (b - a + (a & 1)) // 2
    even_cnt = b - a - odd_cnt
    # print(odd_cnt, even_cnt, x, y)
    return odd_cnt * x + even_cnt * min(x, y)

ans = []
for _ in range(t):
    ans.append(solve())
print('\n'.join(map(str, ans)))