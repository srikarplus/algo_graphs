# Uses python3

import sys
import queue
import heapq
from collections import namedtuple

# https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/#:~:text=Dijkstra%27s%20algorithm%20uses%20a%20priority,of%20vertices%20sorted%20by%20distance.
def distance(adj, cost, s, t):
    n = len(adj)
    dist = [float("inf")] * n
    dist[s] = 0
    # (dist, vertex)
    point = namedtuple("point", "dist vertex")
    pq = [point(0, 0)]

    while pq:
        p = heapq.heappop(pq)
        if p.dist > dist[p.vertex]:
            continue
        for i, v in enumerate(adj[p.vertex]):
            if dist[v] > dist[p.vertex] + cost[p.vertex][i]:
                dist[v] = dist[p.vertex] + cost[p.vertex][i]
                heapq.heappush(pq, (dist[v], v))

    return -1 if dist[t] == float('inf') else dist[t]


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(
        zip(zip(data[0 : (3 * m) : 3], data[1 : (3 * m) : 3]), data[2 : (3 * m) : 3])
    )
    data = data[3 * m :]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
