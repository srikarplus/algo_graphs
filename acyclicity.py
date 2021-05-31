#Uses python3

import sys

# v1 use topological sort method
def acyclic(adj):
    n = len(adj)
    vis = [False] * n
    mem = list()

    def dfs(vertex):
        vis[vertex] = True
        for v in adj[vertex]:
            if not vis[v]:
                dfs(v)
        mem.append(vertex)

    for i in range(n):
        if not vis[i]:
            dfs(i)

    mem.reverse()
    return check_cycle(adj, mem)


def check_cycle(adj, tsort):
    n = len(adj)
    pos = {v: i for i, v in enumerate(tsort)}
    for p in range(n):
        for c in adj[p]:
            parent = 0 if not pos[p] else pos[p]
            child = 0 if not pos[c] else pos[c]

            if parent > child:
                return 1
    return 0

# v2
def acyclic(adj):
    n = len(adj)
    vis = [False] * n
    stk = [False] * n

    def dfs(vertex):
        if stk[vertex]:
            return 1
        vis[vertex] = True
        stk[vertex] = True
        ans = 0
        for v in adj[vertex]:
            if not vis[v]:
                ans |= dfs(v)
            elif stk[v]:
                ans = 1
        stk[vertex] = False
        return 0 or ans

    res = 0
    for v in range(n):
        if not vis[v]:
            res |= dfs(v)
    return 0 or res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)                                                                                                                                                                                                      
    print(acyclic(adj))
