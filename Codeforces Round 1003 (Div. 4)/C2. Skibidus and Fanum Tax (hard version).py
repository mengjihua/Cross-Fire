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

def solve():
    n, m = map(int, input().split())
    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))
    
    b_lst.sort()
    pre = -inf
    
    for num in a_lst:
        min_valid_num = num if num >= pre else inf
            
        pos = bisect_left(b_lst, pre + num)
        if pos < m:
            transformed = b_lst[pos] - num
            min_valid_num = min(min_valid_num, transformed)
        
        if min_valid_num == inf:
            return False
            
        pre = min_valid_num
        
    return True

t = int(input())
ans = []
for _ in range(t):
    ans.append(solve())

for i in ans:
    print('Yes' if i else 'No')
