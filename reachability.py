#Uses python3

import sys

def reach(adj, x, y):
    n = len(adj)
    vis = [False] * n
    def dfs(vertex):
        vis[vertex] = True
        if vertex == y:
            return 1
        ans = 0
        for v in adj[vertex]:
            if not vis[v]:
                ans |= dfs(v)
        return ans
    return 0 or dfs(x)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
