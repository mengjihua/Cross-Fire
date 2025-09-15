import timeit

# 测试数据
text1 = "hello world" * 100
text2 = "hello xorld" * 100

# 方法1: 直接比较字符
def compare_chars():
    s = text1
    t = text2
    count = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:  # 直接比较 str 对象
            count += 1
    return count

# 方法2: 先转换为 ord 列表，再比较
def compare_ord_list():
    s = [ord(c) for c in text1]  # 预转换
    t = [ord(c) for c in text2]
    count = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:  # 比较 int
            count += 1
    return count

# 方法3: 边遍历边转换
def compare_ord_on_fly():
    s = text1
    t = text2
    count = 0
    for i in range(min(len(s), len(t))):
        if ord(s[i]) == ord(t[i]):  # 每次都调用 ord()
            count += 1
    return count

time_char = timeit.timeit(compare_chars, number=10000)
time_ord_list = timeit.timeit(compare_ord_list, number=10000)
time_ord_fly = timeit.timeit(compare_ord_on_fly, number=10000)

print(f"Compare chars:     {time_char:.4f}s")  
print(f"Compare ord list:  {time_ord_list:.4f}s")
print(f"Compare ord fly:   {time_ord_fly:.4f}s")

''' test1:
    Compare chars:     0.8840s
    Compare ord list:  1.5357s
    Compare ord fly:   1.1292s 
'''
''' test2:
    Compare chars:     0.7726s
    Compare ord list:  1.3088s
    Compare ord fly:   0.9509s 
'''