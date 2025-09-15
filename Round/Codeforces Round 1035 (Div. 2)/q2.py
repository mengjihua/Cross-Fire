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
    n = int(input())
    p1, p2, q1, q2 = map(int, input().split())
    a_lst = list(map(int, input().split()))
    
    dis_diff = sqrt((p1 - q1) ** 2 + (p2 - q2) ** 2)
    a_lst.sort()
    a_sum = sum(a_lst)
    
    if a_sum < dis_diff:
        return 'No'
    
    a_max = max(a_lst)
    min_diff = max(0, a_max * 2 - a_sum)

    # print(min_diff, dis_diff, a_sum)
    if min_diff <= dis_diff <= a_sum:
        return "Yes"
    else:
        return "No"


ans = []
for _ in range(t):
    ans.append(solve())
print('\n'.join(map(str, ans)))