

t = int(input())

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    count = 0
    while True:
        count += 1
        step1_done = False
        
        for i in range(n):
            if a[i] > b[i]:
                a[i] -= 1
                step1_done = True
                break
        
        for i in range(n):
            if a[i] < b[i]:
                a[i] += 1
                break
        
        if not step1_done:
            break

    return count

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')