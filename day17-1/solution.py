def get_rocks(rock_input):
  rocks = []
  rock = []
  for line in rock_input.split('\n'):
    if '#' not in line:
      rock.reverse()
      rocks.append(rock)
      rock = []
      continue
    rock.append(list(line))
  rock.reverse()
  rocks.append(rock)
  return rocks

def has_intersection(pos, rock, grid):
  if pos[1] < 0 or pos[1] + len(rock[0]) > 7:
    return True
  for y in range(len(rock)):
    for x in range(len(rock[0])):
      if rock[y][x] == '#' and grid[pos[0] + y][pos[1] + x] == '#':
        return True
  return False

def add_rock(pos, rock, grid):
  for y in range(len(rock)):
    for x in range(len(rock[0])):
      if rock[y][x] == '#':
        grid[pos[0] + y][pos[1] + x] = rock[y][x]
  return grid

def get_height(grid):
  for i, r in enumerate(reversed(grid)):
    if '#' in r:
      return len(grid) - i
  return 0

def get_tower_height(rock_input, jet_input):
  rocks = get_rocks(rock_input)
  jets = [1 if jet == '>' else -1 for jet in list(jet_input)]
  grid = [['#' for _ in range(7)]]
  jet_i = 0
  for rock_i in range(4000):
    rock = rocks[rock_i % len(rocks)]
    pos = (get_height(grid) + 3, 2)
    if pos[0] + len(rock) > len(grid):
      for _ in range(len(grid), pos[0] + len(rock) + 1):
        grid.append(['.' for _ in range(7)])
    down = False
    while True:
      if down:
        new_pos = (pos[0] - 1, pos[1])
        if has_intersection(new_pos, rock, grid):
          grid = add_rock(pos, rock, grid)
          break
        pos = new_pos
      else:
        jet = jets[jet_i % len(jets)]
        jet_i += 1
        new_pos = (pos[0], pos[1] + jet)
        if not has_intersection(new_pos, rock, grid):
          pos = new_pos
      down = not down
  return get_height(grid) - 1
