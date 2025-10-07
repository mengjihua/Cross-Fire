# t = int(input())

# def min_actions(x):
#     binary_x = bin(x)[2:]

#     actions = 0
#     for i, bit in enumerate(reversed(binary_x)):
#         if bit == '1':
#             actions += i + 1
            
#     return actions

# for _ in range(t):
#     x = int(input())
#     print(min_actions(x))

# x ans
# 1 3
# 2 5
# 3 6
# 4 7
# 5 7
# 14 9
t = int(input())

for _ in range(t):
    x = int(input())
    high = 0
    for i in range(1, 31):
        if 2 ** i - 1 >= x:
            high = i
            break
    
    start = 2 * high - 1
    print(start + 2)