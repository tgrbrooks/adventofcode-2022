import math

def divisible(divisor):
  def operator(number):
    return number % divisor == 0
  return operator

def get_operator(op, value):
  if op == '+':
    if value == 'old':
      def operator(number):
        return math.floor((2 * number) / 3)
      return operator
    def operator(number):
      return math.floor((number + int(value))/3)
    return operator
  if op == '*':
    if value == 'old':
      def operator(number):
        return math.floor((number ** 2)/3)
      return operator
    def operator(number):
      return math.floor((number * int(value))/3)
    return operator
  raise ValueError()

class Monkey:
  def __init__(self):
    self.items = []
    self.operation = None
    self.test = None
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
      l += 1
      line = lines[l].split(' ')
      monkey.test_true = int(line[-1])
      l += 1
      line = lines[l].split(' ')
      monkey.test_false = int(line[-1])
      monkeys.append(monkey)
  return monkeys

def get_monkey_business(input):
  monkeys = parse_input(input)
  round = 0
  while round < 20:
    for monkey in monkeys:
      while len(monkey.items):
        item = monkey.items.pop(0)
        item = monkey.operator(item)
        if monkey.test(item):
          monkeys[monkey.test_true].items.append(item)
        else:
          monkeys[monkey.test_false].items.append(item)
        monkey.count += 1
    round += 1
  monkeys.sort(key = lambda x: x.count, reverse=True)
  return monkeys[0].count * monkeys[1].count
