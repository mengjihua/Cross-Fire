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
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    if a[-1] != b[-1]:
        return "NO"
    
    temp = a.copy() 
    for i in range(n - 2, -1, -1):
        if a[i] == b[i]:
            continue
        if a[i] ^ a[i + 1] == b[i]:
            a[i] = a[i] ^ a[i + 1]
        elif a[i] ^ temp[i + 1] == b[i]:
            a[i] = a[i] ^ temp[i + 1]
        else:
            return "NO"
    
    return "YES"

t = int(input())
ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')