def parse_input(input):
  sensors = []
  beacons = set()
  for line in input.split('\n'):
    sx = int(line.split('x=')[1].split(',')[0])
    sy = int(line.split('y=')[1].split(':')[0])
    sensors.append((sx, sy))
    bx = int(line.split('x=')[2].split(',')[0])
    by = int(line.split('y=')[2])
    beacons.add((bx, by))
  return sensors, beacons

def dist(s, b):
  return abs(s[0]-b[0]) + abs(s[1]-b[1])

def overlaps(a, b):
  if b[0] >= a[0] and b[0] <= a[1]:
    return True
  else:
    return False

def merge(arr):
  merged_list= []
  merged_list.append(arr[0])
  for i in range(1, len(arr)):
    pop_element = merged_list.pop()
    if overlaps(pop_element, arr[i]):
      new_element = pop_element[0], max(pop_element[1], arr[i][1])
      merged_list.append(new_element)
    else:
      merged_list.append(pop_element)
      merged_list.append(arr[i])
  return merged_list

def find_beacon(input):
  sensors, beacons = parse_input(input)
  closest = []
  for s in sensors:
    cdist = None
    for b in beacons:
      if cdist is None or dist(s, b) < cdist:
        cdist = dist(s, b)
    closest.append(cdist)
  for row in range(4000000):
    excluded = []
    for i, s in enumerate(sensors):
      drow = closest[i] - dist(s, (s[0], row))
      if drow < 0:
        continue
      excluded.append([max(s[0]-drow, 0), min(s[0]+drow, 4000000)])
    sorted_intervals = sorted(excluded)
    merged = merge(sorted_intervals)
    for i in range(len(merged)-1):
      if merged[i+1][0] - merged[i][1] == 2:
        return (merged[i][1]+1)*4000000 + row
