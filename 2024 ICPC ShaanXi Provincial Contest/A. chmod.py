T = int(input())
temp = ['r', 'w', 'x']

for _ in range(T):
    ans = ''
    s = input()
    for permission in s:
        per_bin = bin(int(permission))[2:]
        per_bin = '0' * (3 - len(per_bin)) + per_bin  # 保持三位数
        # print(permission, per_bin)
        for i in range(3):
            if per_bin[i] == '1':
                ans += temp[i]
            elif per_bin[i] == '0':
                ans += '-'
    print(ans)