def get_signal_strength(input):
  cycle = 0
  register = 1
  sum = 0
  for cmd in input.split('\n'):
    if cycle + 1 in [20, 60, 100, 140, 180, 220]:
      print(cycle + 1, register, (cycle + 1) * register)
      sum += (cycle + 1) * register
    if cmd == 'noop':
      cycle += 1
    if cmd.split(' ')[0] == 'addx':
      if cycle + 2 in [20, 60, 100, 140, 180, 220]:
        print(cycle + 2, register, (cycle + 2) * register)
        sum += (cycle+2) * register
      cycle += 2
      register += int(cmd.split(' ')[1])
  return sum
