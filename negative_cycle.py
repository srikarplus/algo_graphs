#Uses python3

import sys


def negative_cycle(adj, cost, n, m):
    dist = [float('inf')] * n
    dist[0] = 0
    for i in range(n):
        for j in range(n):
            for k, v in enumerate(adj[j]):
                if dist[v] > dist[j] + cost[j][k]:
                    dist[v] = dist[j] + cost[j][k]
                    # dist changed on nth iteration
                    if i == n - 1:
                        return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost, n, m))
