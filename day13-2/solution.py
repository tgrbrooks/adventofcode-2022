import ast

class ToSort:
  def __init__(self, data):
    self.data = data

  def __lt__(self, other):
    if compare_lists(self.data, other.data):
      return True
    return False

def compare_lists(left, right):
  for l_i in range(len(left)):
    if l_i >= len(right):
      return False
    if isinstance(left[l_i], int) and isinstance(right[l_i], int):
      if left[l_i] < right[l_i]:
        return True
      elif right[l_i] < left[l_i]:
        return False
      else:
        continue
    if isinstance(left[l_i], int):
      new_left = [left[l_i]]
    else:
      new_left = left[l_i]
    if isinstance(right[l_i], int):
      new_right = [right[l_i]]
    else:
      new_right = right[l_i]
    next_comp = compare_lists(new_left, new_right)
    if next_comp is not None:
      return next_comp
  if len(right) > len(left):
    return True
  return None

def ordered_index_mult(input):
  lines = input.split('\n')
  unsorted = [ToSort([[2]]), ToSort([[6]])]
  for i in range(0, len(lines), 3):
    unsorted.append(ToSort(ast.literal_eval(lines[i])))
    unsorted.append(ToSort(ast.literal_eval(lines[i+1])))
  unsorted.sort()
  sorted = []
  for s in unsorted:
    sorted.append(s.data)
  return (sorted.index([[2]]) + 1) * (sorted.index([[6]]) + 1)
