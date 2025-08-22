from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b

t = int(input())

def solve():
    n = int(input())
    lst = list(input())
    
    temp = 0
    for i in range(n - 1):
        if lst[i] != lst[i + 1]:
            temp += 1
            
    if temp >= 3:
        return 0
        
    max_add = -inf
    
    for i in range(n):
        add = 0
        if i > 0:
            old_l = 1 if lst[i - 1] != lst[i] else 0
            new_l = 1 if lst[i - 1] == lst[i] else 0
            add += new_l - old_l
        if i < n - 1:
            old_r = 1 if lst[i] != lst[i + 1] else 0
            new_r = 1 if lst[i] == lst[i + 1] else 0
            add += new_r - old_r
            
        if add > max_add:
            max_add = add
            
    if temp + max_add >= 3:
        return 1
    else:
        return 2
    

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')