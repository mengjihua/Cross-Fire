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
    cnt = [0] * 4
    for i in range(n):
        cnt[i % 4] += 1

    judge = cnt[0] == cnt[2] and cnt[1] == cnt[3]
    
    if not judge:
        print("Alice")
    else:
        print("Bob")