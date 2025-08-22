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

a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))

a_sum = a_lst[0] * 2 + sum(a_lst[1:])
b_sum = b_lst[4] * 2 + sum(b_lst[:4])

if a_sum > b_sum:
    print('YES')
else:
    print('NO')