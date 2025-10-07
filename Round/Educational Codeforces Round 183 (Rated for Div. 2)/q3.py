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
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)

t = int(input())

def solve():
    n = int(input())
    s = list(input())
    
    cnt_a = s.count('a')
    cnt_b = s.count('b')

    if cnt_a == cnt_b:
        return 0

    diff = cnt_a - cnt_b
    pre = 0
    dic = {0: -1}
    
    mn_len = inf
    for i, c in enumerate(s):
        if c == 'a':
            pre += 1
        else:
            pre -= 1
        
        target = pre - diff
        
        if target in dic:
            start = dic[target] + 1
            length = i - start + 1
            if length < mn_len:
                mn_len = length
        
        dic[pre] = i
    
    if mn_len == inf or mn_len == n:
        return -1
    return mn_len

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')