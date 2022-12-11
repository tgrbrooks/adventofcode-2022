def divisible(divisor):
  def operator(number):
    return number % divisor == 0
  return operator

def get_operator(op, value):
  if op == '+':
    if value == 'old':
      def operator(number):
        return 2 * number
      return operator
    def operator(number):
      return number + int(value)
    return operator
  if op == '*':
    if value == 'old':
      def operator(number):
        return number ** 2
      return operator
    def operator(number):
      return number * int(value)
    return operator
  raise ValueError()

class Monkey:
  def __init__(self):
    self.items = []
    self.operation = None
    self.test = None
    self.divisor = None
    self.test_true = None
    self.test_false = None
    self.count = 0

def parse_input(input):
  monkeys = []
  lines = input.split('\n')
  for l in range(len(lines)-5):
    if lines[l].split(' ')[0] == 'Monkey':
      monkey = Monkey()
      l += 1
      line = lines[l].split(' ')
      monkey.items.extend([int(line[i].split(',')[0]) for i in range(4, len(line))])
      l += 1
      line = lines[l].split(' ')
      monkey.operator = get_operator(line[-2], line[-1])
      l += 1
      line = lines[l].split(' ')
      monkey.test = divisible(int(line[-1]))
      monkey.divisor = int(line[-1])
      l += 1
      line = lines[l].split(' ')
      monkey.test_true = int(line[-1])
      l += 1
      line = lines[l].split(' ')
      monkey.test_false = int(line[-1])
      monkeys.append(monkey)
  for monkey in monkeys:
    monkey.items = [[item for m in monkeys] for item in monkey.items]
  return monkeys

def get_monkey_business(input):
  monkeys = parse_input(input)
  round = 0
  while round < 10000:
    for m, monkey in enumerate(monkeys):
      while len(monkey.items):
        item = monkey.items.pop(0)
        item = [monkey.operator(item[i]) for i in range(len(monkeys))]
        for i in range(len(monkeys)):
          if monkeys[i].test(item[i]):
            item[i] = monkeys[i].divisor
        if monkey.test(item[m]):
          monkeys[monkey.test_true].items.append(item)
        else:
          monkeys[monkey.test_false].items.append(item)
        monkey.count += 1
    round += 1
  monkeys.sort(key = lambda x: x.count, reverse=True)
  return monkeys[0].count * monkeys[1].count
