def count_contained(input):
  contained = 0
  for pair in input.split('\n'):
    p1 = pair.split(',')[0].split('-')
    p2 = pair.split(',')[1].split('-')
    if (int(p1[0]) >= int(p2[0]) and int(p1[1]) <= int(p2[1])) or (int(p2[0]) >= int(p1[0]) and int(p2[1]) <= int(p1[1])):
      contained += 1
  return contained
