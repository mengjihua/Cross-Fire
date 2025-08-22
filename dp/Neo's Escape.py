import sys
import bisect

def solve():
    t = int(input())
    
    results = []
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        # 求最长非递减子序列（Longest Non-Decreasing Subsequence）
        lis = []
        for num in a:
            # 找第一个大于 num 的位置
            pos = bisect.bisect_right(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num
        results.append(str(len(lis)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    solve()