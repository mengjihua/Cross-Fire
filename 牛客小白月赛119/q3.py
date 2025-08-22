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


def solve():
    n = int(input())
    a_lst = list(map(int, input().split()))
    

ans = []
t = int(input())
for _ in range(t):
    ans.append(solve())
    
for i in ans:
    print(i)