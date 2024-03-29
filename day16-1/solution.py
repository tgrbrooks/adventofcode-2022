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
  scores = [0]
  for name, valve in valves.items():
    if valve.flow != 0 and name not in visited:
      if (time - dists[name] - 1) > 0:
        score = valve.flow * (time-dists[name]-1) + max_score(valves, name, time-dists[name]-1, deepcopy(visited), nonzero)
        scores.append(score)
  return max(scores)

def get_maximum_pressure(input):
  valves = parse_input(input)
  nonzero = set(['AA'])
  for name, valve in valves.items():
    if valve.flow != 0:
      nonzero.add(name)
  start = 'AA'
  time = 30
  return max_score(valves, start, time, set(), nonzero)
