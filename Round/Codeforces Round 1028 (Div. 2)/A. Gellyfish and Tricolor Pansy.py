t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())
    a, b = min(a, c), min(b, d)
    if a >= b:
        print('Gellyfish')
    else:
        print('Flower')