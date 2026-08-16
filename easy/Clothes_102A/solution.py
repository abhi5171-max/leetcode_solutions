import sys

input = sys.stdin.readline

n, m = map(int, input().split())

price = list(map(int, input().split()))

graph = [[] for _ in range(n)]
connected = [[False] * n for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    graph[u].append(v)
    graph[v].append(u)

    connected[u][v] = True
    connected[v][u] = True


INF = float('inf')
answer = INF

for i in range(n):
    neighbors = graph[i]

    # Check every pair of neighbors of i
    for x in range(len(neighbors)):
        j = neighbors[x]

        for y in range(x + 1, len(neighbors)):
            k = neighbors[y]

            # j and k must also match
            if connected[j][k]:
                total = price[i] + price[j] + price[k]
                answer = min(answer, total)

if answer == INF:
    print(-1)
else:
    print(answer)