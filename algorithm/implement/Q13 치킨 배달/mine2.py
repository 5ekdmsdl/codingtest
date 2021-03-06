from itertools import combinations
import math

house = []
chicken = []
chick_dist = []
true_chicken = []
answer = int(1e9)

def chicken_distance(h,chicken_list):
  dist = int(1e9)
  for c in chicken_list:
    d = abs(h[0] - c[0]) + abs(h[1] - c[1])
    if d < dist:
      dist = d
      [x,y] = c
  return dist, [x,y]

n,m = map(int,input().split())

for i in range(n):
  line = list(map(int,input().split()))
  for j in range(n):
    if line[j] == 1:
      house.append((i,j))
    elif line[j] == 2:
      chicken.append((i,j))

# n,m = 5,3d
# house = [(0,2),(1,4),(2,1),(3,2)]
# chicken = [(1,2),(2,2),(4,4)]

# n,m = 5,2
# house = [(0,3),(1,0),(1,2),(3,3),(3,4),(4,3)]
# chicken = [(0,1),(3,0),(4,0),(4,1),(4,4)]ㅇ

# n,m = 5,1
# house = [(0,0),(1,0),(2,0),(3,0),(4,0)]
# chicken = [(0,1),(1,1),(2,1),(3,1),(4,1)]

# n,m = 5,1
# house = [(0,0),(1,0),(2,0),(3,0),(4,0),(0,4),(1,4),(2,4),(3,4),(4,4)]
# chicken = [(0,1),(1,1),(2,1),(3,1),(4,1),(0,3),(1,3),(2,3),(3,3),(4,3)]

for h in house:
  dist, xy = chicken_distance(h, chicken)
  chick_dist.append([dist,xy])
  true_chicken.append(xy)

a = len(true_chicken)
if a <= m:
  answer = 0
  for i in chick_dist:
    answer += i[0]
  print(answer)
else:
  com_t = combinations(true_chicken,m)

  for c in com_t:
    total = 0
    for h in house:
      dist, xy = chicken_distance(h,c)
      total += dist
    answer = min(answer, total)
  print(answer)
