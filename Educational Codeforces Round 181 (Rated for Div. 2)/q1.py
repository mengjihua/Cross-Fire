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

t = int(input())

def solve():
    s = input()
    count = Counter(s)
    
    # 判断原字符串是否不含FFT或NTT
    if 'FFT' not in s and 'NTT' not in s:
        return s
    
    if count['F'] >= 1 and count['N'] >= 1:
        temp = 'N' * (count['N'] - 1) + 'F' * (count['F'] - 1) + 'N' + 'F'
        for k, v in count.items():
            if k != 'F' and k != 'N':
                temp += k * v
        return temp
    elif count['F'] >= 1:
        temp = 'T' * count['T']
        for k, v in count.items():
            if k != 'T':
                temp += k * v
        return temp
    elif count['N'] >= 1:
        temp = 'T' * count['T']
        for k, v in count.items():
            if k != 'T':
                temp += k * v
        return temp
    else:
        return s
        


ans = []
for _ in range(t):
    ans.append(solve())

for s in ans:
    print(s)