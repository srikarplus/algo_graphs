#Uses python3

import sys
import queue
from collections import deque

def bipartite(adj):
    n = len(adj)
    q = deque()
    q.append(0)
    col = [None] * n
    col[0] = 1

    while q:
        tmp = q.popleft()
        tmpc = col[tmp]
        for i in adj[tmp]:
            if col[i]:
                if col[i] == tmpc:
                    return 0
            else:
                col[i] = tmpc ^ 1
                q.append(i)
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
