def get_image(input):
  crt = [['.' for i in range(40)] for j in range(6)]
  cycle = 0
  register = 1
  for cmd in input.split('\n'):
    row = (cycle) // 40
    col = (cycle) % 40
    if register >= (col - 1) and register <= (col + 1):
      crt[row][col] = '#'
    if cmd == 'noop':
      cycle += 1
    if cmd.split(' ')[0] == 'addx':
      row = (cycle + 1) // 40
      col = (cycle + 1) % 40
      if register >= (col - 1) and register <= (col + 1):
        crt[row][col] = '#'
      cycle += 2
      register += int(cmd.split(' ')[1])
  for r in crt:
    print(''.join(r))
