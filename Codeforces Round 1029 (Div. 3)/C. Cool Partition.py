from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    a_lst = list(map(int, input().split()))
    
    cnt = 1
    # 上一个子数组的元素计数
    last_sub_set = set(a_lst[:1])
    # 当前子数组的元素计数
    cur_sub_set = set()
    for i in range(1, n):
        # 更新
        cur_sub_set.add(a_lst[i])
        # 如果当前元素在上一个子序列中，减少计数, 为0则删除
        if a_lst[i] in last_sub_set:
            last_sub_set.remove(a_lst[i])
        # 判断当前元素是否包含了上一个子数组的所有元素
        if not last_sub_set:
            last_sub_set = cur_sub_set
            cur_sub_set = set()
            cnt += 1
        
    print(cnt)