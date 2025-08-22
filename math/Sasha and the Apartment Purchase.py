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
    n, k = map(int, input().split())
    # T = (n - k + 1) // 2 是成为中位数所需的最小酒吧覆盖数
    T = (n - k + 1) // 2
    a_lst = list(map(int, input().split()))
    
    cnt = Counter(a_lst)
    distinct = sorted(cnt.keys())
    s = len(distinct)
    
    prefix_sum = [0] * s
    suffix_sum = [0] * s
    
    prefix_sum[0] = cnt[distinct[0]]
    for i in range(1, s):
        prefix_sum[i] = prefix_sum[i - 1] + cnt[distinct[i]]
    
    suffix_sum[s - 1] = cnt[distinct[s - 1]]
    for i in range(s - 2, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + cnt[distinct[i]]
    
    ans = 0
    for i in range(s):
        m_val = min(prefix_sum[i], suffix_sum[i])
        if m_val >= T:
            ans += 1
    
    for i in range(s - 1):
        m_gap = min(prefix_sum[i], suffix_sum[i + 1])
        if m_gap >= T:
            gap_length = distinct[i + 1] - distinct[i] - 1
            if gap_length > 0:
                ans += gap_length
    print(ans)



t = int(input())
for _ in range(t):
    solve()