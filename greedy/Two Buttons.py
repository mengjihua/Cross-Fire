# bfs
from collections import deque

n, m = map(int, input().split())

ans = 0
if n >= m:
    print(n - m)
else:
    q = deque()
    q.append((n, 0))
    visited = set()
    visited.add(n)
    while q:
        n, depth = q.popleft()
        if n == m:
            ans = depth
            break
        if n + 1 <= m and n + 1 not in visited:
            visited.add(n + 1)
            q.append((n + 1, depth + 1))
        if n * 2 <= m and n * 2 not in visited:
            visited.add(n * 2)
            q.append((n * 2, depth + 1))

print(ans)