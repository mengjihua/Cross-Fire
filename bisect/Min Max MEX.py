import sys

def compute_global_mex(arr):
    max_possible = len(arr) + 2
    present = [False] * max_possible
    for num in arr:
        if 0 <= num < max_possible:
            present[num] = True
    mex = 0
    while present[mex]:
        mex += 1
    return mex

def check(v, k, m):
    cnt = 0
    current_set = set()
    cur_mex = 0
    max_relevant = len(v) + 1  # 过滤无关大数
    for x in v:
        if x <= max_relevant:
            current_set.add(x)
        # 更新当前MEX
        while cur_mex in current_set:
            cur_mex += 1
        # 满足条件则分割
        if cur_mex >= m:
            cnt += 1
            current_set = set()
            cur_mex = 0
    return cnt >= k

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, k = int(input[ptr]), int(input[ptr + 1])
        ptr += 2
        v = list(map(int, input[ptr:ptr + n]))
        ptr += n
        # 二分查找最大值m
        ans, left, right = 0, 0, compute_global_mex(v)
        while right >= left:
            mid = (left + right) // 2
            if check(v, k, mid):
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
        print(ans)

if __name__ == "__main__":
    main()