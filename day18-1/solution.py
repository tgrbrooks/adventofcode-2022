def count_surface_area(input):
  cubes = []
  for line in input.split('\n'):
    cube = line.split(',')
    cubes.append((int(cube[0]), int(cube[1]), int(cube[2])))
  sides = len(cubes) * 6
  for cube in cubes:
    for dx in range(-1, 2, 1):
      for dy in range (-1, 2, 1):
        for dz in range(-1, 2, 1):
          if dx == dy == dz == 0:
            continue
          if abs(dx) + abs(dy) + abs(dz) > 1:
            continue
          if (cube[0] + dx, cube[1] + dy, cube[2] + dz) in cubes:
            sides -= 1
  return sides
