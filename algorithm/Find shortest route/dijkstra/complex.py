import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# n,m = map(int,input().split())
n, m = 6, 11

# start = int(input())
start = 1

graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

# for _ in range(m):
#   a, b, c = map(int,input().split())
#   graph[a].append((b,c))
graph = [[],[(2,2),(3,5),(4,1)],[(3,3),(4,2)],[(2,3),(6,5)],[(3,3),(5,1)],[(3,1),(6,2)],[]]


def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])
