def parse_input(input):
  tree_array = []
  for r in input.split('\n'):
    row = []
    for c in r:
      row.append(c)
    tree_array.append(row)
  return tree_array

def get_score(tree, view):
  score = 0
  for t in view:
    score += 1
    if t >= tree:
      return score
  return score

def max_scenic_score(input):
  tree_array = parse_input(input)
  columns = list(zip(*tree_array))
  max_score = 0
  for r in range(len(tree_array)):
    for c in range(len(tree_array[0])):
      tree = tree_array[r][c]
      scorel = get_score(tree, tree_array[r][:c][::-1])
      scorer = get_score(tree, tree_array[r][c+1:])
      scoreu = get_score(tree, columns[c][:r][::-1])
      scored = get_score(tree, columns[c][r+1:])
      score = scorel * scorer * scoreu * scored
      if score > max_score:
        max_score = score
  return max_score
