from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sys import setrecursionlimit, stdin, stdout
from random import getrandbits
setrecursionlimit(5 * 10 ** 4 + 1)
input = lambda: stdin.readline().rstrip()
RD = getrandbits(31)
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b

t = int(input())

# TODO: 优化
def solve():
    n, y = map(int, input().split())
    c = list(map(int, input().split()))
    
    mx = max(c)
    ans = -inf
    
    for x in range(2, mx + 2):
        new = [ceil(price / x) for price in c]
        
        temp = Counter(new)
        count = Counter(c)
        
        print_cost = 0
        for price, cnt in temp.items():
            cc = count[price]
            if cnt > cc:
                print_cost += (cnt - cc)
        
        sm = sum(new) - print_cost * y
        if sm > ans:
            ans = sm
    
    return ans
    

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')