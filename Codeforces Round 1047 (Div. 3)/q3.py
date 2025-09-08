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
from random import getrandbits
setrecursionlimit(5 * 10 ** 4 + 1)
input = lambda: stdin.readline().rstrip()
RD = getrandbits(31)
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b


t = int(input())

def solve():
    a, b = map(int, input().split())
    
    if a % 2 == 0:
        if b % 2 == 1:
            return -1
        else:
            temp1 = a + b
            temp2 = a * (b // 2) + 2
            return _max(temp1, temp2)
    else:
        if b % 2 == 0:
            cnt = 0
            temp = b
            while temp % 2 == 0:
                cnt += 1
                temp //= 2
            if cnt == 1:
                return -1
            else:
                return a * (b // 2) + 2
        else:
            return a * b + 1


ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')