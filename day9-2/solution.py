import math

def distance(head, tail):
  return math.sqrt(math.pow(head[0]-tail[0], 2) + math.pow(head[1] - tail[1], 2))

def move(rope, dir, dist, visited):
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
    rope[0] = (rope[0][0] + move[0], rope[0][1] + move[1])
    for r in range(1, len(rope)):
      if distance(rope[r-1], rope[r]) >= 2:
        horiz = 0 if rope[r-1][0] == rope[r][0] else 1 if rope[r-1][0] > rope[r][0] else -1
        diag = 0 if rope[r-1][1] == rope[r][1] else 1 if rope[r-1][1] > rope[r][1] else -1
        rope[r] = (rope[r][0] + horiz, rope[r][1] + diag)
        if r == 9:
          visited.add(rope[9])
  return rope, visited

def count_positions(input):
  rope = [(0, 0) for i in range(10)]
  visited = { rope[9] }
  for mv in input.split('\n'):
    rope, visited = move(rope, mv.split(' ')[0], int(mv.split(' ')[1]), visited)
  return len(visited)
