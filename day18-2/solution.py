def get_neighbours(pos):
  neighbours = []
  for dx in range(-1, 2, 1):
    for dy in range (-1, 2, 1):
      for dz in range(-1, 2, 1):
        if dx == dy == dz == 0:
          continue
        if abs(dx) + abs(dy) + abs(dz) > 1:
          continue
        neighbours.append((pos[0] + dx, pos[1] + dy, pos[2] + dz))
  return neighbours

def get_valid_neighbours(pos, cubes):
  valid = []
  for neighbour in get_neighbours(pos):
    if neighbour not in cubes:
      valid.append(neighbour)
  return valid

def dfs(pos, visited, cubes, limits):
  visited.add(pos)
  if not limits.contained(pos):
    raise ValueError('Outside')
  for adj in get_valid_neighbours(pos, cubes):
    if adj not in visited:
      dfs(adj, visited, cubes, limits)

def is_internal(adj, cubes, limits):
  # Expand outwards until cube boundary or hit a cube
  visited = set()
  try:
    dfs(adj, visited, cubes, limits)
  except ValueError as e:
    return False
  return True

class Limits:
  def __init__(self, xs, ys, zs):
    self.min_x = min(xs)
    self.max_x = max(xs)
    self.min_y = min(ys)
    self.max_y = max(ys)
    self.min_z = min(zs)
    self.max_z = max(zs)
  
  def contained(self, pos):
    if (pos[0] < self.min_x):
      return False
    if (pos[0] > self.max_x):
      return False
    if (pos[1] < self.min_y):
      return False
    if (pos[1] > self.max_y):
      return False
    if (pos[2] < self.min_z):
      return False
    if (pos[2] > self.max_z):
      return False
    return True

def count_surface_area(input):
  cubes = []
  xs = []
  ys = []
  zs = []
  for line in input.split('\n'):
    cube = line.split(',')
    cubes.append((int(cube[0]), int(cube[1]), int(cube[2])))
    xs.append(int(cube[0]))
    ys.append(int(cube[1]))
    zs.append(int(cube[2]))
  limits = Limits(xs, ys, zs)
  sides = len(cubes) * 6
  for cube in cubes:
    for adj in get_neighbours(cube):
      if adj in cubes:
        sides -= 1
      elif is_internal(adj, cubes, limits):
        sides -= 1
  return sides
