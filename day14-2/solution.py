def create_grid(input):
  walls = []
  min_y = 0
  min_x = -1
  max_y = 0
  max_x = 0
  for line in input.split('\n'):
    prev_vtx = None
    for vtx in line.split(' -> '):
      vertex = (int(vtx.split(',')[0]), int(vtx.split(',')[1]))
      if vertex[0] > max_x:
        max_x = vertex[0]
      if vertex[1] > max_y:
        max_y = vertex[1]
      if min_x == -1 or vertex[0] < min_x:
        min_x = vertex[0]
      walls.append(vertex)
      if prev_vtx is not None:
        if prev_vtx[0] == vertex[0]:
          for i in range(min(prev_vtx[1], vertex[1]) + 1, max(prev_vtx[1], vertex[1])):
            walls.append((vertex[0], i))
        if prev_vtx[1] == vertex[1]:
          for i in range(min(prev_vtx[0], vertex[0]) + 1, max(prev_vtx[0], vertex[0])):
            walls.append((i, vertex[1]))
      prev_vtx = vertex
  grid = [['.' for _ in range(0, 2*max_x)] for _ in range(min_y, max_y+3)]
  for wall in walls:
    grid[wall[1]][wall[0]] = '#'
  for i in range(len(grid[0])):
    grid[max_y+2][i] = '#'
  return grid, 500, 0

def out_of_grid(x, y, grid):
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
      return True
    return False

def is_clear(x, y, grid):
  if grid[y][x] != '#' and grid[y][x] != 'o':
    return True
  return False

def move_sand(grid, start_x, start_y):
  sand_pos = (start_x, start_y)
  while True:
    if out_of_grid(sand_pos[0], sand_pos[1]+1, grid):
      raise ValueError
    if is_clear(sand_pos[0], sand_pos[1]+1, grid):
      sand_pos = (sand_pos[0], sand_pos[1]+1)
      continue
    if out_of_grid(sand_pos[0]-1, sand_pos[1]+1, grid):
      raise ValueError
    if is_clear(sand_pos[0]-1, sand_pos[1]+1, grid):
      sand_pos = (sand_pos[0]-1, sand_pos[1]+1)
      continue
    if out_of_grid(sand_pos[0]+1, sand_pos[1]+1, grid):
      raise ValueError
    if is_clear(sand_pos[0]+1, sand_pos[1]+1, grid):
      sand_pos = (sand_pos[0]+1, sand_pos[1]+1)
      continue
    return sand_pos

def count_sand(input):
  grid, start_x, start_y = create_grid(input)
  sand_units = 0
  while True:
    sand_pos = move_sand(grid, start_x, start_y)
    if sand_pos[0] == start_x and sand_pos[1] == start_y:
      break
    grid[sand_pos[1]][sand_pos[0]] = 'o'
    sand_units += 1
  return sand_units
