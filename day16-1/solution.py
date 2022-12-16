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
  scores = [0]
  for name, valve in valves.items():
    if valve.flow != 0 and name not in visited:
      time -= (dists[name] + 1)
      if time > 0:
        if pos == 'AA':
          print(pos, name, valve.flow * time)
        score = valve.flow * time + max_score(valves, name, time, deepcopy(visited), nonzero)
        scores.append(score)
        if pos == 'AA':
          print(pos, name, time, score)
    if visited == nonzero or time <= 0:
      if pos == 'AA':
        print(pos, scores)
      return max(scores)
  if pos == 'AA':
    print(pos, scores)
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

input = '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II'''

print(get_maximum_pressure(input))