def parse_input(input):
  grid = []
  start = (0, 0)
  end = (0, 0)
  for i, r in enumerate(input.split('\n')):
    row = []
    for j, c in enumerate(r):
      if c == 'S':
        start = (i, j)
        row.append(0)
      elif c == 'E':
        end = (i, j)
        row.append(25)
      else:
        row.append(ord(c) - ord('a'))
    grid.append(row)
  return grid, start, end

def get_moves(pos, grid):
  moves = []
  for i in range(-1, 2):
    for j in range(-1, 2):
      move = (pos[0] + i, pos[1] + j)
      if move[0] < 0 or move[1] < 0 or move[0] >= len(grid) or move[1] >= len(grid[0]):
        continue
      if grid[pos[0]][pos[1]] - grid[move[0]][move[1]]  > 1:
        continue
      if move[0] == pos[0] and move[1] == pos[1]:
        continue
      if move[0] != pos[0] and move[1] != pos[1]:
        continue
      moves.append(move)
  return moves

def find_path(input):
  grid, start, end = parse_input(input)
  visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
  dist = [[-1 for j in range(len(grid[0]))] for i in range(len(grid))]
  queue = [end]
  visited[end[0]][end[1]] = True
  dist[end[0]][end[1]] = 0
  while len(queue) != 0:
    pos = queue.pop(0)
    for move in get_moves(pos, grid):
      if visited[move[0]][move[1]] == False:
        visited[move[0]][move[1]] = True
        dist[move[0]][move[1]] = dist[pos[0]][pos[1]] + 1
        queue.append(move)
        if grid[move[0]][move[1]] == 0:
          return dist[move[0]][move[1]]
  return None
