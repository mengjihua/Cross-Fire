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

print(log(10 ** 9, 3))
MX = 20

t = int(input())

pow3 = [1] * (MX + 2)
for i in range(1, MX + 2):
    pow3[i] = pow3[i - 1] * 3

cost = [0] * MX
cost[0] = 3 
for i in range(1, MX):
    cost[i] = pow3[i + 1] + i * pow3[i - 1]

def solve():
    n = int(input())
    num_digit = [0] * MX
    for i in range(MX):
        num_digit[i] = n % 3
        n //= 3
    res = 0
    for i in range(MX):
        res += num_digit[i] * cost[i]
    return res

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')