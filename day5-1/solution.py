def parse_input(input):
  n_stacks = (len(input.split('\n')[0]) + 1)//4
  stacks = [[] for _ in range(n_stacks)]
  for line in input.split('\n'):
    if line[1] == '1':
      break
    for n in range(n_stacks):
      if line[4*n + 1] != ' ':
        stacks[n].append(line[4*n + 1])
  return stacks

def get_order(input):
  stacks = parse_input(input)
  for line in input.split('\n'):
    if 'move' not in line:
      continue
    move = line.split(' ')
    num = int(move[1])
    from_stack = int(move[3]) - 1
    to_stack = int(move[5]) - 1
    for _ in range(num):
      stacks[to_stack].insert(0, stacks[from_stack].pop(0))
  for i in range(len(stacks)):
    print(stacks[i].pop(0))
