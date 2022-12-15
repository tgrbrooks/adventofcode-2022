def parse_input(input):
  sensors = []
  beacons = []
  for line in input.split('\n'):
    sx = int(line.split('x=')[1].split(',')[0])
    sy = int(line.split('y=')[1].split(':')[0])
    sensors.append((sx, sy))
    bx = int(line.split('x=')[2].split(',')[0])
    by = int(line.split('y=')[2])
    beacons.append((bx, by))
  return sensors, beacons

def dist(s, b):
  return abs(s[0]-b[0]) + abs(s[1]-b[1])

def count_excluded(input, row):
  sensors, beacons = parse_input(input)
  closest = []
  for s in sensors:
    cdist = dist(s, beacons[0])
    for b in beacons[1:]:
      if dist(s, b) < cdist:
        cdist = dist(s, b)
    closest.append(cdist)
  excluded = set()
  for i, s in enumerate(sensors):
    drow = closest[i] - dist(s, (s[0], row))
    if drow < 0:
      continue
    # Loop from closest[i] in row to (s[0], row)
    for x in range(-drow, drow+1):
      e = (s[0]+x, row)
      if e not in beacons:
        excluded.add(e)
  count = 0
  for e in excluded:
    if e[1] == row:
      count += 1
  return count

input = '''Sensor at x=391282, y=2038170: closest beacon is at x=-532461, y=2166525
Sensor at x=3042382, y=3783761: closest beacon is at x=3113582, y=3814857
Sensor at x=3444090, y=757238: closest beacon is at x=2930045, y=2000000
Sensor at x=971638, y=288172: closest beacon is at x=935006, y=638195
Sensor at x=2175844, y=1879176: closest beacon is at x=2930045, y=2000000
Sensor at x=3063103, y=3820576: closest beacon is at x=3113582, y=3814857
Sensor at x=2591294, y=3667337: closest beacon is at x=2768198, y=3762135
Sensor at x=2579773, y=3989626: closest beacon is at x=2768198, y=3762135
Sensor at x=2887876, y=2106773: closest beacon is at x=2930045, y=2000000
Sensor at x=2808659, y=3280271: closest beacon is at x=2768198, y=3762135
Sensor at x=2874212, y=3897058: closest beacon is at x=2768198, y=3762135
Sensor at x=720384, y=134640: closest beacon is at x=935006, y=638195
Sensor at x=489, y=1241813: closest beacon is at x=-532461, y=2166525
Sensor at x=120643, y=2878973: closest beacon is at x=227814, y=3107489
Sensor at x=3990734, y=2991891: closest beacon is at x=3924443, y=3039680
Sensor at x=1494086, y=3030634: closest beacon is at x=2537630, y=2793941
Sensor at x=1864417, y=360451: closest beacon is at x=935006, y=638195
Sensor at x=2974807, y=3732804: closest beacon is at x=3113582, y=3814857
Sensor at x=3273340, y=3998032: closest beacon is at x=3113582, y=3814857
Sensor at x=1468886, y=1597081: closest beacon is at x=935006, y=638195
Sensor at x=2083016, y=3743849: closest beacon is at x=2768198, y=3762135
Sensor at x=3387080, y=3393862: closest beacon is at x=3113582, y=3814857
Sensor at x=2959440, y=2052862: closest beacon is at x=2930045, y=2000000
Sensor at x=1180804, y=1112043: closest beacon is at x=935006, y=638195
Sensor at x=2829808, y=2206448: closest beacon is at x=2930045, y=2000000
Sensor at x=3999024, y=3114260: closest beacon is at x=3924443, y=3039680
Sensor at x=540955, y=3893312: closest beacon is at x=227814, y=3107489
Sensor at x=3669058, y=2350731: closest beacon is at x=3924443, y=3039680
Sensor at x=2915068, y=2754266: closest beacon is at x=2537630, y=2793941
Sensor at x=3507419, y=2838686: closest beacon is at x=3924443, y=3039680
Sensor at x=165939, y=498589: closest beacon is at x=935006, y=638195
Sensor at x=3917917, y=3792648: closest beacon is at x=3924443, y=3039680
Sensor at x=40698, y=3202257: closest beacon is at x=227814, y=3107489
Sensor at x=2619948, y=2439745: closest beacon is at x=2537630, y=2793941'''

print(count_excluded(input, 10))