def get_delay_time(times, N, K):
    INF = float('inf')
    dist = [INF for _ in range(N)]
    dist[K] = 0
    for _ in range(N):
        for u, v, w in times:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    time = max(dist)
    return time if time is not INF else -1


    
def get_data():
    N = int(input().strip())
    connection = int(input().strip())
    return N, connection

#input
# N, connection = get_data()
# i = 0
# times = []
# while i < N - 1:
#     u, v, w = list(map(int, input().strip().split()))
#     times.append((u-1, v-1, w))
#     i += 1
# K = int(input().strip()) - 1

#exp1
N = 4
connection = 3
times = [(1, 0, 1), (1, 2, 1), (2, 3, 1)]
K = 1
print(f'N:{N}, connection:{connection}, times:{times}, K:{K}')

print(f'\n answer:{get_delay_time(times, N, K)}')
