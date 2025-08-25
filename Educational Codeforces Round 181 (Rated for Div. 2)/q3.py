from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

t = int(input())

def solve():
    l, r = map(int, input().split())
    l -= 1
    temp_l, temp_r = 0, 0
    # print('-' * 50)
    for i in '2357':
        temp_l += l // int(i)
        temp_r += r // int(i)
    # print(temp_l, temp_r)
    for i in [2 * 3, 2 * 5, 2 * 7, 3 * 5, 3 * 7, 5 * 7]:
        temp_l -= l // int(i)
        temp_r -= r // int(i)
    # print(temp_l, temp_r)
    for i in [2 * 3 * 5, 2 * 3 * 7, 2 * 5 * 7, 3 * 5 * 7]:
        temp_l += l // int(i)
        temp_r += r // int(i)
    # print(temp_l, temp_r)
    temp_l -= l // (2 * 3 * 5 * 7)
    temp_r -= r // (2 * 3 * 5 * 7)
    # print(temp_l, temp_r)
    # print('-' * 50)
    return r - temp_r - (l - temp_l)
    
ans = []
for _ in range(t):
    ans.append(solve())

for i in ans:
    print(i)