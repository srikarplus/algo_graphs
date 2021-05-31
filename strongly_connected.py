#Uses python3

import sys

sys.setrecursionlimit(200_000)


def reverse_graph(adj):
    n = len(adj)
    rev = [[] for _ in range(n)]
    for i in range(n):
        for j in range(len(adj[i])):
            rev[adj[i][j]].append(i)
    return rev


def dfs(adj, used, post_order, x):
    used[x] = True
    for v in adj[x]:
        if not used[v]:
            dfs(adj, used, post_order, v)
    post_order.append(x)



def number_of_strongly_connected_components(adj):
    result = 0
    rev_adj = reverse_graph(adj)
    n = len(adj)
    used = [False] * n
    post_order = list()
    for i in range(n):
        if not used[i]:
            dfs(rev_adj, used, post_order, i)
    post_order.reverse()

    used = [False] * n
    for v in post_order:
        if not used[v]:
            dfs(adj, used, [], v)
            result += 1

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
