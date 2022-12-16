from copy import deepcopy

class Valve:
  def __init__(self, name, flow, connections):
    self.name = name
    self.flow = int(flow)
    self.connections = [c for c in connections.split(', ')]

def parse_input(input):
  valves = {}
  for line in input.split('\n'):
    name = line.split('Valve ')[1].split(' ')[0]
    connections = line.split('valves ')[1] if 'valves' in line else line.split('valve ')[1]
    valves[name] = Valve(name, line.split('rate=')[1].split(';')[0], connections)
  return valves

def get_distances(valves, start):
  visited = {name: False for name in valves.keys()}
  dist = {name: -1 for name in valves.keys()}
  queue = [valves[start]]
  visited[start] = True
  dist[start] = 0
  while len(queue) != 0:
    valve = queue.pop(0)
    for connection in valve.connections:
      if visited[connection] == False:
        visited[connection] = True
        dist[connection] = dist[valve.name] + 1
        queue.append(valves[connection])
  return dist

def max_score(valves, pos, time, visited, nonzero):
  dists = get_distances(valves, pos)
  visited.add(pos)
  if time <= 0 or visited == nonzero:
    return 0
  # Go to every non-zero valve, open it, add to score
  # For each connected non zero valve get it's score
  print_pos = 'AA'
  scores = [0]
  for name, valve in valves.items():
    if valve.flow != 0 and name not in visited:
      if (time - dists[name] - 1) > 0:
        if pos == print_pos:
          print(pos, name, valve.flow * (time-dists[name]-1))
        score = valve.flow * (time-dists[name]-1) + max_score(valves, name, time-dists[name]-1, deepcopy(visited), nonzero)
        scores.append(score)
        if pos == print_pos:
          print(pos, name, time-dists[name]-1, score)
  return max(scores)

def get_maximum_pressure(input):
  valves = parse_input(input)
  nonzero = set(['AA'])
  for name, valve in valves.items():
    if valve.flow != 0:
      nonzero.add(name)
  # starting at AA
  # Calculate distance to every non-zero valve (bfs)
  start = 'AA'
  time = 30
  return max_score(valves, start, time, set(), nonzero)

input = '''Valve TZ has flow rate=0; tunnels lead to valves ZJ, DM
Valve LH has flow rate=0; tunnels lead to valves FP, IS
Valve AA has flow rate=0; tunnels lead to valves XU, JH, CD, WY, HK
Valve GP has flow rate=0; tunnels lead to valves BO, KL
Valve GN has flow rate=0; tunnels lead to valves QO, FP
Valve QO has flow rate=0; tunnels lead to valves CA, GN
Valve JT has flow rate=22; tunnel leads to valve BL
Valve DF has flow rate=0; tunnels lead to valves BO, HK
Valve UM has flow rate=0; tunnels lead to valves OS, LE
Valve KJ has flow rate=0; tunnels lead to valves YF, UK
Valve UX has flow rate=23; tunnels lead to valves WM, ZI
Valve ZI has flow rate=0; tunnels lead to valves UX, AR
Valve YF has flow rate=0; tunnels lead to valves KJ, EK
Valve SX has flow rate=0; tunnels lead to valves DM, CD
Valve KZ has flow rate=0; tunnels lead to valves FR, LE
Valve IH has flow rate=0; tunnels lead to valves DM, IE
Valve EL has flow rate=0; tunnels lead to valves WQ, BO
Valve CD has flow rate=0; tunnels lead to valves AA, SX
Valve OR has flow rate=0; tunnels lead to valves FP, IR
Valve EK has flow rate=19; tunnels lead to valves YF, LK
Valve UE has flow rate=0; tunnels lead to valves FP, LG
Valve WQ has flow rate=0; tunnels lead to valves EL, DM
Valve XI has flow rate=0; tunnels lead to valves YH, DM
Valve GO has flow rate=0; tunnels lead to valves BO, CQ
Valve IR has flow rate=0; tunnels lead to valves ZJ, OR
Valve WY has flow rate=0; tunnels lead to valves UI, AA
Valve JH has flow rate=0; tunnels lead to valves AA, CA
Valve WM has flow rate=0; tunnels lead to valves UX, YH
Valve OS has flow rate=0; tunnels lead to valves UM, CA
Valve AE has flow rate=0; tunnels lead to valves FP, YH
Valve LG has flow rate=0; tunnels lead to valves UE, LE
Valve IS has flow rate=0; tunnels lead to valves LH, AR
Valve XU has flow rate=0; tunnels lead to valves AA, TU
Valve KL has flow rate=0; tunnels lead to valves GP, TU
Valve LV has flow rate=0; tunnels lead to valves UK, TU
Valve UI has flow rate=0; tunnels lead to valves ZJ, WY
Valve IL has flow rate=0; tunnels lead to valves GW, LK
Valve XY has flow rate=0; tunnels lead to valves AZ, CA
Valve JF has flow rate=15; tunnels lead to valves FR, BK
Valve UK has flow rate=18; tunnels lead to valves LV, KJ
Valve CA has flow rate=13; tunnels lead to valves JH, XY, QO, BK, OS
Valve BL has flow rate=0; tunnels lead to valves JT, GW
Valve GW has flow rate=16; tunnels lead to valves IL, BL
Valve CQ has flow rate=0; tunnels lead to valves ZJ, GO
Valve HK has flow rate=0; tunnels lead to valves DF, AA
Valve BO has flow rate=4; tunnels lead to valves GO, GP, EL, DF
Valve TU has flow rate=11; tunnels lead to valves XU, IE, KL, LV
Valve AZ has flow rate=0; tunnels lead to valves ZJ, XY
Valve FP has flow rate=5; tunnels lead to valves GN, AE, UE, LH, OR
Valve LE has flow rate=14; tunnels lead to valves KZ, LG, UM
Valve IE has flow rate=0; tunnels lead to valves IH, TU
Valve NZ has flow rate=0; tunnels lead to valves YH, AR
Valve DM has flow rate=3; tunnels lead to valves WQ, IH, TZ, SX, XI
Valve YH has flow rate=21; tunnels lead to valves WM, NZ, AE, XI
Valve BK has flow rate=0; tunnels lead to valves JF, CA
Valve LK has flow rate=0; tunnels lead to valves EK, IL
Valve AR has flow rate=20; tunnels lead to valves IS, NZ, ZI
Valve ZJ has flow rate=9; tunnels lead to valves IR, AZ, TZ, UI, CQ
Valve FR has flow rate=0; tunnels lead to valves JF, KZ'''

print(get_maximum_pressure(input))