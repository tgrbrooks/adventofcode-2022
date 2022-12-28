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

def get_signature(grid):
  sig = ''
  i = 0
  for r in reversed(grid):
    if '#' in r:
      sig += ''.join(r)
      i += 1
    if i == 30:
      return sig
  return sig

def calculate_height(starts, start, prev_height, rock_i, total, heights):
  start_height = starts[start][0]
  start_blocks = starts[start][1]
  cycle_height = prev_height - starts[start][0]
  cycle_blocks = rock_i - starts[start][1]
  height = start_height + cycle_height * ((total - start_blocks)//cycle_blocks)
  remaining_blocks = total - (start_blocks + cycle_blocks * ((total - start_blocks)//cycle_blocks))
  cycle_heights = []
  for i in range(cycle_blocks-1):
    cycle_heights.append(heights[rock_i - i - 1] - heights[rock_i - i - 2])
  cycle_heights.append(heights[rock_i] - heights[rock_i - 1])
  cycle_heights.reverse()
  for i in range(remaining_blocks):
    height += cycle_heights[i]
  return height

def get_tower_height(rock_input, jet_input):
  rocks = get_rocks(rock_input)
  jets = [1 if jet == '>' else -1 for jet in list(jet_input)]
  grid = [['#' for _ in range(7)]]
  jet_i = 0
  starts = {}
  total = 1000000000000
  prev_height = 0
  heights = []
  for rock_i in range(total):
    rock = rocks[rock_i % len(rocks)]
    pos = (get_height(grid) + 3, 2)
    ## If height + rock height larger than grid, extend grid
    if pos[0] + len(rock) > len(grid):
      for _ in range(len(grid), pos[0] + len(rock) + 1):
        grid.append(['.' for _ in range(7)])
    down = False
    while True:
      if down:
        new_pos = (pos[0] - 1, pos[1])
        # Check for intersection with grid
        if has_intersection(new_pos, rock, grid):
          prev_height = get_height(grid) - 1
          grid = add_rock(pos, rock, grid)
          heights.append(get_height(grid) - 1)
          signature = get_signature(grid)
          start = (rock_i % len(rocks), jet_i % len(jets))
          if start in starts and signature == starts[start][2]:
            return calculate_height(starts, start, prev_height, rock_i, total, heights) 
          starts[start] = (prev_height, rock_i, signature)
          break
        pos = new_pos
      else:
        jet = jets[jet_i % len(jets)]
        jet_i += 1
        new_pos = (pos[0], pos[1] + jet)
        # Check for intersection with grid
        if not has_intersection(new_pos, rock, grid):
          pos = new_pos
      down = not down
  return get_height(grid) - 1
