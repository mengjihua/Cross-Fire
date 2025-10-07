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
    n, k = map(int, input().split())
    s = list(input())
    
    res = ['+'] * n
    zero_cnt, one_cnt, two_cnt = s.count('0'), s.count('1'), s.count('2')
    
    if k == n:
        return '-' * n
    
    for i in range(zero_cnt, zero_cnt + two_cnt):
        res[i] = '?'
    for i in range(n - (one_cnt + two_cnt), n - one_cnt):
        res[i] = '?'
    for i in range(zero_cnt):
        res[i] = '-'
    for i in range(n - one_cnt, n):
        res[i] = '-'
        
    return ''.join(res)
        

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')