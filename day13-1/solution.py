import ast

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

def count_ordered(input):
  sum = 0
  lines = input.split('\n')
  for i in range(0, len(lines), 3):
    left = ast.literal_eval(lines[i])
    right = ast.literal_eval(lines[i+1])
    if compare_lists(left, right):
      sum += (i//3) + 1
  return sum
