import math

def distance(head, tail):
  return math.sqrt(math.pow(head[0]-tail[0], 2) + math.pow(head[1] - tail[1], 2))

def move(head, tail, dir, dist, visited):
  move = (0, 0)
  if dir == 'U':
    move = (0, 1)
  if dir == 'D':
    move = (0, -1)
  if dir == 'L':
    move = (-1, 0)
  if dir == 'R':
    move = (1, 0)
  for _ in range(dist):
    head = (head[0] + move[0], head[1] + move[1])
    if distance(head, tail) >= 2:
      tail = (head[0] - move[0], head[1] - move[1])
      visited.add(tail)
  return head, tail, visited

def count_positions(input):
  head = (0, 0)
  tail = (0, 0)
  visited = { tail }
  for mv in input.split('\n'):
    head, tail, visited = move(head, tail, mv.split(' ')[0], int(mv.split(' ')[1]), visited)
  return len(visited)
