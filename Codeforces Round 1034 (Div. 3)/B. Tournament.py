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
    n, j, k = map(int, input().split())
    a_lst = list(map(int, input().split()))
    
    judge_num = a_lst[j - 1]
    
    a_lst.sort(reverse=True)
    
    if k == 1:
        if a_lst[0] == judge_num:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')