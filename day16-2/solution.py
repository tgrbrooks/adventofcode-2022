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

def max_score(valves, pos1, pos2, time1, time2, visited, nonzero):
  dists1 = get_distances(valves, pos1)
  dists2 = get_distances(valves, pos2)
  visited.add(pos1)
  visited.add(pos2)
  if time1 <= 0 or time2 <= 0 or visited == nonzero:
    return 0
  scores = [0]
  for name1, valve1 in valves.items():
    if valve1.flow != 0 and name1 not in visited:
        if (time1 - dists1[name1] - 1) > 0:
          score = valve1.flow * (time1-dists1[name1]-1)
          # All valves visited
          for name2, valve2 in valves.items():
            if valve2.flow != 0 and name2 not in visited and name2 != name1:
              if (time2 - dists2[name2] - 1) > 0:
                score = valve1.flow * (time1-dists1[name1]-1) + valve2.flow * (time2-dists2[name2]-1)
                ms = max_score(valves, name1, name2, time1-dists1[name1]-1, time2-dists2[name2]-1, deepcopy(visited), nonzero)
                score += ms
                scores.append(score)
          scores.append(score)
  return max(scores)

def get_maximum_pressure(input):
  valves = parse_input(input)
  nonzero = set(['AA'])
  for name, valve in valves.items():
    if valve.flow != 0:
      nonzero.add(name)
  start = 'AA'
  time = 26
  return max_score(valves, start, start, time, time, set(), nonzero)
