def parse_input(input):
  tree_array = []
  for r in input.split('\n'):
    row = []
    for c in r:
      row.append(c)
    tree_array.append(row)
  return tree_array

def count_visible(input):
  tree_array = parse_input(input)
  columns = list(zip(*tree_array))
  visible = 0
  for r in range(1, len(tree_array)-1):
    for c in range(1, len(tree_array[0])-1):
      tree = tree_array[r][c]
      maxl = max(tree_array[r][:c])
      maxr = max(tree_array[r][c+1:])
      maxu = max(columns[c][:r])
      maxd = max(columns[c][r+1:])
      if tree > maxl or tree > maxr or tree > maxu or tree > maxd:
        visible += 1
  return visible + 2*len(tree_array) + 2*len(tree_array[0]) - 4
