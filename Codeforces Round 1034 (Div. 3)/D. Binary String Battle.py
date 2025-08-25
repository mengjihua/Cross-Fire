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

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    # if len(s) < 2 * k:
    #     print('Alice')
    #     continue
    
    # intervals_cnt = 0
    # cur_one_sum = 0
    # judge = False
    # for i in range(n):
    #     if s[i] == '1':
    #         judge = True
    #         cur_one_sum += 1
    #     else:
    #         if judge or cur_one_sum == k:
    #             intervals_cnt += 1
    #             cur_one_sum = 0
    #             judge = False
    # intervals_cnt += ceil(cur_one_sum / k)
    
    # # print(intervals_cnt, cur_one_sum)
    # if intervals_cnt < 2:
    #     print('Alice')
    # else:
    #     print('Bob')
    
    
    # ones = [i for i, ch in enumerate(s) if ch == '1']
    
    # if not ones or len(ones) < k or len(s) < 2 * k:
    #     print("Alice")
    #     continue
    
    # q = deque()
    # max_ones = idx = 0
    # for i in range(n):
    #     while idx < len(ones) and ones[idx] < i + k:
    #         q.append(ones[idx])
    #         idx += 1
        
    #     while q and q[0] < i:
    #         q.popleft()
        
    #     max_ones = max(max_ones, len(q))
        
    #     if max_ones >= k:
    #         break
    
    # print("Bob" if max_ones >= k else "Alice")
    
    one_cnt = s.count('1')
    if one_cnt <= k or len(s) < 2 * k:
        print('Alice')
    else:
        print('Bob')