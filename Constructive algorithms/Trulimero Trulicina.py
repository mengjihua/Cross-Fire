import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n,m,k = map(int,input().split())
    LAST = [-1 for _ in range(m)]
    
    for i in range(n):
        shift = False
        CUR = [0 for _ in range(m)]
        
        for j in range(m):
            elm = ((i * m + j) % k) + 1
            if elm == LAST[j]:
                shift = True
                break
            CUR[j] = elm
            
        if shift:
            CUR = [LAST[(j+1)%m] for j in range(m)]
            
        print(*CUR)
        LAST = CUR