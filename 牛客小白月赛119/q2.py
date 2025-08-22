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
    lst = list(map(int, input().split()))
    a_lst, k = lst[:5], lst[5]
    temp = 1000
    
    if sum(a_lst) != 0 and k not in a_lst:
        cnt = 0
        temp = 1
    elif sum(a_lst) == 0:
        cnt = 1
    else:
        cnt = a_lst.count(k)
        temp = 5 - a_lst.count(0)
    
    g = gcd(cnt, temp)
    # print(g, cnt, temp)
    cnt //= g
    temp //= g
    
    return f'{cnt}/{temp}'
    

ans = []
t = int(input())
for _ in range(t):
    ans.append(solve())
    
for i in ans:
    print(i)