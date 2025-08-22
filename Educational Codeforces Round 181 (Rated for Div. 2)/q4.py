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

n, m = map(int, input().split())

def inv(x, mod):
    return pow(x, mod - 2, mod)
# print(5 * inv(18, 998244353) % 998244353)

for i in range(n):
    pass
    l, r, p, q = map(int, input().split())